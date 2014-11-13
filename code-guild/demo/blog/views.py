import json

from django.views import generic
from django.http import HttpResponse, Http404

from models import BlogPost, Comment
# Create your views here.


class BlogIndex(generic.ListView):
    queryset = BlogPost.objects.published()
    template_name = "blog_home.html"
    context_object_name = "blog_posts"

def vote(request):
    if request.is_ajax() and request.POST:
	data = {}
	blog = BlogPost.objects.get(pk=request.POST.get("blogId", ''))
        if request.POST.get("vote") == "up":
	    blog.upvotes += 1
	    blog.save()
	    data["votes"] = blog.upvotes
	    return HttpResponse(json.dumps(data), content_type="application/json")	
        if request.POST.get("vote") == "down":
	    blog.downvotes += 1
	    blog.save()
	    data["votes"] = blog.downvotes
	    return HttpResponse(json.dumps(data), content_type="application/json")
    else:
	return Http404		
	
