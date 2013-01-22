import random

from imagecreator import settings


def color_hex_to_dec(color):
    if color.startswith('#'):
        color = color[1:]
    return int(color, 16)


def random_color():
    random_color = hex(random.randrange(settings.RGB_COMBS))[2:]
    # Set zeros
    random_color = '#' + ('0' * (6 - len(random_color))) + random_color
    return random_color


def check_size(size):
    """Checks if the size is correct"""
    try:
        for i in size:
            if i < settings.SIZE_MIN or i > settings.SIZE_MAX:
                return False
        return True
    except Exception:
        return False


def check_color_str(str_color):
    try:
        return True if settings.COLOR_REGEX.search(str_color) else False
    except Exception:
        return False


def check_color_int(int_color):
    try:
        for i in int_color:
            if i < settings.COLOR_MIN or i > settings.COLOR_MAX:
                return False

        return True
    except Exception:
        return False


def check_color(color):
    if isinstance(color, int):
        return check_color_int(color)
    else:
        return check_color_str(color)
