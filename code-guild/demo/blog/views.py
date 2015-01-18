import json
import datetime

from django.views.generic import ListView, DetailView
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response, RequestContext
from django.core.serializers import serialize

from endless_pagination.decorators import page_template
from .models import BlogPost, Comment


@page_template("blog_post_template.html")
def blog_index(request, template="blog_home.html", extra_context=None):
    context = {"blog_posts": BlogPost.objects.all()}
    if extra_context is not None:
	context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))


def blog_post_detail(request, *args, **kwargs):
    blog_post = get_object_or_404(BlogPost, pk=kwargs.get("pk"))
    response = {"blog_post": blog_post}
    return render_to_response('blog_detail.html', response)


def vote(request):
    if request.is_ajax() and request.POST:
	data = {}
	blog = BlogPost.objects.get(pk=request.POST.get("blogId", ""))
        if request.POST.get("vote") == "up":
	    blog.upvotes += 1
	    blog.save()
	    data["votes"] = blog.upvotes
	    data["vote"] = "up"
	    data["id"] = blog.id
	    return HttpResponse(json.dumps(data), content_type="application/json")	
        if request.POST.get("vote") == "down":
	    blog.downvotes += 1
	    blog.save()
	    data["votes"] = blog.downvotes
	    data["vote"] = "down"
	    data["id"] = blog.id
	    return HttpResponse(json.dumps(data), content_type="application/json")
    else:
	return Http404		
	

def add_comment(request):
    if request.is_ajax() and request.method == "POST":
	data = {}
	blog = BlogPost.objects.get(pk=request.POST.get("blogId", ""))
	comment = request.POST.get("comment", "")
	new_comment = Comment(blog=blog, body=comment)
	new_comment.save()
	data.update({"comment": new_comment.body, "blogId": blog.id, "commentId": new_comment.id})
	return HttpResponse(json.dumps(data), content_type="application/json")


def get_comments(request):
    if request.is_ajax() and request.method == "GET":
	blog = BlogPost.objects.get(pk=request.GET.get("blogId", ""))
	comments = serialize("json", Comment.objects.filter(blog=blog.id))
	return HttpResponse(comments, content_type="application/json")


