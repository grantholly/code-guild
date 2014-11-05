from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages

from .forms import SignUpForm
from .models import SignUp
# Create your views here.

def signup(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        save_post = form.save()
        messages.success(request, "You are signed up!")

    return render_to_response("signup.html", locals(),
                               context_instance=RequestContext(request))
