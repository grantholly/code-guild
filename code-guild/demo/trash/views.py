from django.shortcuts import render, render_to_response


def trash_index(request):
    return render_to_response('trash_home.html')
