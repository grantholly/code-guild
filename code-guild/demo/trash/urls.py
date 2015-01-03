from django.conf.urls import patterns, url

from . import views
from .views import Upload

urlpatterns = patterns('',
    url(r'^$', views.trash_index, name='index'),
    url(r'upload/$', Upload.as_view(), name='upload'),
)

