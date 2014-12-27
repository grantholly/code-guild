import json
import datetime

from django.views.generic import ListView, DetailView
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.core.serializers import serialize
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import BlogPost, Comment


class BlogIndex(ListView):
    queryset = BlogPost.objects.published()
    paginate_by = 2
    template_name = "blog_home.html"
    context_object_name = "blog_posts"


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


def search(request):
    query = request.GET.get("query", "")
    # todo - check for query in post body, comment body, or by tag
    results = BlogPost.objects.filter(body__contains=query)
    return HttpResponse(results, content_type="application/json")


@ensure_csrf_cookie
def get_blogs(request):
    if request.is_ajax() and request.method == "GET":
	last_blog = request.GET.get("lastBlog", "")
	"""incoming format = "Thursday, 04:40 AM nov 06, 2014"
	date must match 2014-11-06T04:40:49.984795+0000 """
	last_blog = datetime.datetime.strptime(last_blog, "%A, %I:%M %p %b %d, %Y")
	blogs = serialize("json", BlogPost.objects.filter(created__lte = last_blog)[:2])
        return HttpResponse(blogs, content_type="application/json")
