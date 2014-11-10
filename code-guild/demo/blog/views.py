import json

from django.views import generic
from django.http import HttpResponse, Http404

from models import BlogPost
# Create your views here.


class BlogIndex(generic.ListView):
    queryset = BlogPost.objects.published()
    template_name = "blog_home.html"

def vote(request):
    if not request.method == "POST":
	raise Http404
    response = {}
    blog_post_id = request.POST.get("blogId", "")
    vote = request.POST.get("vote", "")
    blog = BlogPost.objects.get(pk=blog_post_id)
    if blog:
	if vote == "up":
	    blog.upvotes += 1
	    response["votes"] = blog.upvotes
	    blog.save()
	if vote == "down":
	    blog.downvotes += 1
	    response["votes"] = blog.downvotes
	    blog.save()
    json.dumps(response)
    return HttpResponse(response, content_type="application/json")
