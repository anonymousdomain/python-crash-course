import unittest
from python.crash_course_try.chapter_11.module_being_tested.city import get_cty_country

class TestCity(unittest.TestCase):
    def test_city(self):
        f=get_cty_country('ethiopia','addis abeba',5000)
        self.assertEqual(f,'Ethiopia ,Addis Abeba population-5000')