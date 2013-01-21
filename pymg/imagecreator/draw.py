import StringIO

import Image
import ImageDraw

import utils
from imagecreator.drawexceptions import DrawException, SizeException


class Figure(object):

    def __init__(self, width=None, height=None, color=None, alpha=None):
        self.width = width
        self.height = height
        self.color = color
        self.alpha = alpha
        self._img = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not utils.check_size((value,)):
            raise SizeException("The width is out of bounds or not correct")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not utils.check_size((value,)):
            raise SizeException("The height is out of bounds or not correct")
        self._height = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not utils.check_color(value):
            raise DrawException()

        if not value.startswith('#'):
            value = "#{0}".format(value)
        self._color = value

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = value

    def draw():
        raise NotImplementedError()

    def save(self, name, format="PNG"):
        self._img.save(name, format)

    def get_img_data(self, format="PNG"):
        output = StringIO.StringIO()
        self._img.save(output, format=format)
        str_img = output.getvalue()
        output.close()
        return str_img


class Square(Figure):

    def draw(self):
        size = (self._width, self.height)
        #TODO: Use alpha
        self._img = Image.new("RGB", size, self._color)
        return self._img


class Circle(Figure):

    def __init__(self, radius=None, color=None, alpha=None):
        self._draw = None
        self._radius = radius
        super(Circle, self).__init__(radius, radius, color, alpha)

    def draw(self):
        size = (self._width, self.height)

        # Use the alpha for the background
        self._img = Image.new("RGBA", size, (0, 0, 0, 0))

        #TODO: Use alpha
        draw = ImageDraw.Draw(self._img)
        draw.ellipse((0, 0, self._radius, self._radius), fill=self._color)

        return self._img
