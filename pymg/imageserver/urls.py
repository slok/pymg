from django.conf.urls import patterns, url

import imageserver.views

urlpatterns = patterns('',

    # /c/100x200
    url(r'c/(?P<radius>\d+)$',
        imageserver.views.draw_circle_width_height,
        name="draw_circle_width_height"),

    # /100x200
    url(r'(?P<width>\d+)x(?P<height>\d+)$',
        imageserver.views.draw_square_width_height,
        name="draw_square_width_height"),

    # /
    url(r'$', imageserver.views.index, name="index"),
)
