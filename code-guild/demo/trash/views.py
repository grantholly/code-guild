import json

from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, DeleteView, ListView
from django.http import HttpResponse, Http404
from django.core.context_processors import csrf
from django.core.files.uploadedfile import UploadedFile

from .models import Document
from .response import JSONResponse, response_mimetype
from .serialize import serialize


def index(request):
    token = {}
    token.update(csrf(request))
    return render_to_response("trash_home.html", token)


def upload(request):
    """
    key: u'file_', #like file_0 or file_1
    value: [<InMemoryUploadedFile: Eva-Green-Sin-City-a-Dame-to-Kill-For.jpg (image/jpeg)>]}>,
        type: MultiValueDict
        request.FILES[u"files"].__dict__:

    {'file': <_io.BytesIO object at 0x7eff18698530>, 
    'content_type_extra': {}, 
    'charset': None, 
    '_name': u'Eva-Green-Sin-City-a-Dame-to-Kill-For.jpg', 
    'content_type': u'image/jpeg', 
    '_size': 335411, 
    'field_name': u'files[]'}
    """
    if request.method == "POST" and request.FILES:
	if request.FILES == None:
	    return HttpResponse("<h1>No files sent!</h1>")

	new_files = []
	for image in request.FILES:
	    #pulling files out of request and putting them into UploadedFile instances
	    file = UploadedFile(request.FILES[image])
	    file_name = request.FILES[image]._name
	    file_size = request.FILES[image]._size
	    
            #putting uploaded files into our DB
	    upload = Document()
	    upload.file_name = str(file_name)
	    upload.document = file
	    upload.size = file_size
	    upload.file_type = upload.get_file_type()
	    new_files.append(upload)
	
	#create all files in one DB transaction from a list of Document instances
	Document.objects.bulk_create(new_files)

	# todo return a serialized JSON of the files to the browser for thumbnails
        return HttpResponse("<h1>You did it!</h1>")
