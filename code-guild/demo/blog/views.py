import json

from django.views import generic
from django.http import HttpResponse, Http404
from django.core.serializers import serialize

from .models import BlogPost, Comment


class BlogIndex(generic.ListView):
    queryset = BlogPost.objects.published()
    template_name = "blog_home.html"
    context_object_name = "blog_posts"


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
    # todo - check for query in post body and/or comment body
    results = BlogPost.objects.filter(body__contains=query)
    return HttpResponse(results, content_type="application/json")
