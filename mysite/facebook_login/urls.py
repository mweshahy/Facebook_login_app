from django.conf.urls import patterns, include, url

from facebook_login import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.home),
    url(r'^logout/$', views.logout),
    url(r'^done/$', views.done, name='done'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
)