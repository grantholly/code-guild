from django.views import generic

from . import models
# Create your views here.


class BlogIndex(generic.ListView):
    queryset = models.BlogPost.objects.published()
    template_name = "blog_home.html"

def upvote(request):
    # handler for XHR POST request

def downvote(request):
    # handler for XHR POST request
