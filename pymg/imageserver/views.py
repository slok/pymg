from django.shortcuts import (render_to_response,
                             RequestContext)
from django.http import HttpResponse

from imagecreator import utils
from imagecreator.draw import Square


def index(request):
    data = {
    }
    return render_to_response('imageserver/index.html',
                            data,
                            context_instance=RequestContext(request))


def draw_width_height(request, width, height):
    #Create the image
    width, height = int(width), int(height)
    color = utils.random_color()
    s = Square(width, height, color)
    s.draw()

    #Get the content of the image in memory
    data = s.get_img_data()

    return HttpResponse(data, content_type="image/png")
