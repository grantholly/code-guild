from django.shortcuts import render, render_to_response

# Create your views here.

def blog_index(request):
    context = {}
    return render_to_response('blog.html', context)


def post(request):
    context = {}
    return render_to_response('write_post.html', context)

class DetailView(generic.DetailView):
    model = BlogPost
    template = ''
