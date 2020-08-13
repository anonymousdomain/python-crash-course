import unittest
from python.crash_course_try.chapter_11.module_being_tested.formatted_name import get_formatted_name


class TestFormattedName(unittest.TestCase):
    def test_first_last(self):
        formatted_name = get_formatted_name('dawit','yitagesu')
        self.assertEqual(formatted_name,'Dawit Yitagesu')

    def test_first_middle_last(self):
        formatted_name = get_formatted_name('dawit', 'yitagesu','mekonnen')
        self.assertEqual(formatted_name, 'Dawit Mekonnen Yitagesu')
if __name__ == "__main__":
    unittest.main