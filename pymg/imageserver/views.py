from django.shortcuts import (render_to_response,
                             RequestContext)
from django.http import HttpResponse

from imagecreator import utils
from imagecreator.draw import Square, Circle


def index(request):
    data = {
    }
    return render_to_response('imageserver/index.html',
                            data,
                            context_instance=RequestContext(request))


def draw_square_width_height(request, width, height, color):
    #check if is a square (two sides equal)
    if not height:
        height = width

    if not color:
        color = utils.random_color()
    #Create the image
    width, height = int(width), int(height)

    s = Square(width, height, color)
    return draw_factory(s)


def draw_circle_width_height(request, radius):
    #Create the image
    radius = int(radius)
    color = utils.random_color()
    s = Circle(radius, color)
    return draw_factory(s)


def draw_factory(img):
    img.draw()

    #Get the content of the image in memory
    data = img.get_img_data()

    return HttpResponse(data, content_type="image/png")
