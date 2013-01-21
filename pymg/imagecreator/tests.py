from django.test import TestCase

from imagecreator import utils
from imagecreator import settings


class TestUtils(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check_size(self):
        size = (128, 128)
        self.assertTrue(utils.check_size(size))

        wrong_size1 = (-100, 128)
        wrong_size2 = (128, 9999999999)

        self.assertFalse(utils.check_size(wrong_size1))
        self.assertFalse(utils.check_size(wrong_size2))

    def test_check_color_str(self):
        self.assertTrue(utils.check_color_str("A1f"))
        self.assertFalse(utils.check_color_str("A6G"))
        self.assertTrue(utils.check_color_str("ABCDEF"))
        self.assertTrue(utils.check_color_str("A2C3E7"))
        self.assertTrue(utils.check_color_str("A2C3E7"))
        self.assertTrue(utils.check_color_str("#A2C3E7"))
        self.assertFalse(utils.check_color_str("A2C3E"))
        self.assertFalse(utils.check_color_str("A2C3E7S"))

    def test_check_color_int(self):
        self.assertTrue(utils.check_color_int((1, 2, 3, 4, 5)))
        self.assertTrue(utils.check_color_int((1, 2, 3, 4, 255)))
        self.assertTrue(utils.check_color_int((1, 2, 3, 4, 0)))
        self.assertFalse(utils.check_color_int((1, 2, 3, -2, 0)))
        self.assertFalse(utils.check_color_int((1, 2, 3, -2, 256)))

    def test_check_color(self):
        self.assertFalse(utils.check_color((1, 2, 3, -2, 0)))
        self.assertFalse(utils.check_color((1, 2, 3, -2, 256)))
        self.assertTrue(utils.check_color("A1f"))
        self.assertFalse(utils.check_color("A6G"))

    def test_random_color(self):
        self.assertTrue(utils.color_hex_to_dec(utils.random_color()) <\
                             settings.RGB_COMBS)
