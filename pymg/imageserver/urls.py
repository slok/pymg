from django.conf.urls import patterns, url

import imageserver.views

urlpatterns = patterns('',
    url(r'$', imageserver.views.index, name="index"),
)
