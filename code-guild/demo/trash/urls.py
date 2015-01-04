from django.conf.urls import patterns, url

from . import views
# from .views import Upload

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'upload/$', views.upload, name='upload'),
    url(r'edit/$', views.edit, name='edit'),
    url(r'delete/$', views.delete, name='delete'),
)

