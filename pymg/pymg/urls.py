from django.conf.urls import patterns, include, url

import imageserver.urls


urlpatterns = patterns('',
    url(r'^', include(imageserver.urls)),
)
