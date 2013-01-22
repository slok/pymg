from django.conf.urls import patterns, url

import imageserver.views

urlpatterns = patterns('',

    # /
    url(r'^$', imageserver.views.index, name="index"),

    # /100x200 or /s/100x200
    url(r'^(s/)?(?P<width>\d+)x(?P<height>\d+)$',
        imageserver.views.draw_square_width_height,
        name="draw_square_width_height"),

    # /c/100x200
    url(r'^c/(?P<radius>\d+)$',
        imageserver.views.draw_circle_width_height,
        name="draw_circle_width_height"),


)
