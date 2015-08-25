from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from . import views

admin.autodiscover()
urlpatterns = patterns('',

    # authentication urls
    url(r'^login/$', views.login, name='login'),
    url(r'^authenticate/$', views.authenticate, name='authenticate'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login_success/$', views.login_success, name='login_success'),
    url(r'^invalid/$', views.invalid, name='invalid'),
                       
    # password recovery urls
    url(r'^password_recover/', include('password_reset.urls')),

    # registration urls
    url(r'^register/$', views.register, name='register'),
    url(r'^register_success/$', views.register_success, name='register_success'),
    
    # signup urls
    url(r'^$', include('signups.urls', namespace='signups', app_name='signups')),

    # blog urls
    url(r'^blogs/', include('blog.urls', namespace='blog', app_name='blog')),

    # trash urls
    url(r'^trash/', include('trash.urls', namespace='trash', app_name='trash')),

    # search urls
    url(r'^search/', include('search.urls', namespace='search', app_name='search')),
                       
    # admin urls
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
	url(r'^__debug__/', include(debug_toolbar.urls)),
)
