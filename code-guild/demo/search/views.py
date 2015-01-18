from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core import serializers

from blog.models import BlogPost


class Search(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            query_string = request.GET["query"]
            blogs = BlogPost.objects.filter(title__contains=query_string)
            data = serializers.serialize("json", blogs)
            return HttpResponse(data, content_type="application/json")