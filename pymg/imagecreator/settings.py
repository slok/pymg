import re

from django.conf import settings


SIZE_MAX = getattr(settings, 'SIZE_MAX', 1000)
SIZE_MIN = getattr(settings, 'SIZE_MIN', 1)

COLOR_MAX = getattr(settings, 'COLOR_MAX', 255)
COLOR_MIN = getattr(settings, 'COLOR_MIN', 0)

RGB_COMBS = getattr(settings, 'RGB_COMBS', 16777216)

COLOR_REGEX = getattr(settings, 'COLOR_REGEX',
                        re.compile("^#?([A-Fa-f\d]{3}|[A-Fa-f\d]{6})$"))
