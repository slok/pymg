from django.shortcuts import (render_to_response,
                             RequestContext)


def index(request):
    data = {
    }
    return render_to_response('imageserver/index.html',
                            data,
                            context_instance=RequestContext(request))


def draw_width_height(request, width, height):
    print(width)
    print(height)
    return render_to_response('imageserver/index.html',
                            context_instance=RequestContext(request))
