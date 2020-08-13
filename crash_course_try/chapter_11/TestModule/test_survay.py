import unittest
from crash_course_try.chapter_11.module_being_tested.survay import AnonymousSurvay


class TestAnonymousClass(unittest.TestCase):

    def setUp(self):
        question = "What language did you first learn to?\n"
        self.survay = AnonymousSurvay(question)
        self.responses = ['amharic', 'english', 'french']

    def test_single_responses(self):
        """test that it store a single responses properly"""

        self.survay.stor_responses(self.responses[0])
        self.assertIn(self.responses[0], self.survay.responeses)

    def test_three_responses(self):

        for response in self.responses:
            self.survay.stor_responses(response)
        for response in self.responses:
            self.assertIn(response, self.survay.responeses)


if __name__ == '__main__':
    unittest
