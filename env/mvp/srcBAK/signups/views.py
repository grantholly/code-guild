from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.

from .forms import SignUpForm


def home(request):
    
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    
    return render_to_response("signup.html", locals(),
                              context_instance=RequestContext(request))