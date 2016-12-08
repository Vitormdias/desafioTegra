import unittest
from classes.main import Developer

class DeveloperTestCase(unittest.TestCase):
    def setUp(self):
        self.developer = Developer("Vitor","Intern")

    def test_presentation(self):
        expected = "Hello I am Vitor and I am a Intern"
        self.assertEqual(expected, self.developer.presentation())

if __name__ == '__main__':
    unittest.main()
