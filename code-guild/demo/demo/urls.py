from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',

    # authentication urls
    url(r'^login/$', 'demo.views.login', name='login'),
    url(r'^authenticate/$', 'demo.views.authenticate', name='authenticate'),
    url(r'^logout/$', 'demo.views.logout', name='logout'),
    url(r'^login_success/$', 'demo.views.login_success', name='login_success'),
    url(r'^invalid/$', 'demo.views.invalid', name='invalid'),

    # registration urls
    url(r'^register/$', 'demo.views.register', name='register'),
    url(r'^register_success/$', 'demo.views.register_success', name='register_success'),
    
    # signup urls
    url(r'^$', include('signups.urls')),

    # blog urls
    url(r'^blogs/', include('blog.urls')),

    # admin urls
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
)
