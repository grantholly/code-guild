from django.views import generic
from django.template import RequestContext
from django.http import HttpResponse

from . import models
# Create your views here.


class BlogIndex(generic.ListView):
    queryset = models.BlogPost.objects.published()
    template_name = "blog_home.html"

def vote(request):
    if not request.POST:
	return render_to_response("blog_home.html", {})
    xhr = request.GET.has_key("xhr")
    response = {}
    blog_post_id = request.POST.get("blogId", False)
    vote = request.POST.get("vote", False)
    response.update({"blog_post_id": blog_post_id, "vote": vote})
    if blog_post_id and vote:
	blog = models.BlogPost.objects.get(pk=blog_post_id)
	if vote == "up":
            blog.upvotes += 1
	    response["votes"] = blog.upvotes
	if vote == "down":
	    blog.downvotes += 1
	    response["votes"] = blog.downvotes
	blog.save()
    if xhr:
	print(request.POST)
	return HttpResponse(response, mimetype="application/json")
    # return HttpResponse(response)
	    	
