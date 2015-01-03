import json

from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, DeleteView, ListView
from django.http import HttpResponse

from .models import Document
from .response import JSONResponse, response_mimetype
from .serialize import serialize


def trash_index(request):
    return render_to_response('trash_home.html')


class Upload(CreateView):
    model = Document

    def form_valid(self, form):
	files = [serialize(form.save())]
	data = {'files': files}
	response = JSONResponse(data, mimetype=response_mimetype(self.request))
	response["Content-Disposition"] = "inline; filename=files.json"
	return response

    def form_valid(self, form):
	data = json.dumps(form.errors)
	return HttpResponse(content=data, status=400, content_type="application/json")
