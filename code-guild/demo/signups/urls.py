from django.conf.urls import patterns, url


urlpatterns = patterns('',
    #signup urls
    url(r'^$', 'signups.views.signup', name='signup'),
)
