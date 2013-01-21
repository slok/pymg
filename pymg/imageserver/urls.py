from django.conf.urls import patterns, url

import imageserver.views

urlpatterns = patterns('',
    # /100x200
    url(r'(?P<width>\d+)x(?P<height>\d+)$', imageserver.views.draw_width_height,
                                            name="draw_width_height"),
    # /
    url(r'$', imageserver.views.index, name="index"),
)
