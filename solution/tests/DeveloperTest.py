import unittest
from classes.Developer import Developer

class DeveloperTestCase(unittest.TestCase):
    def setUp(self):
        self.developer = Developer("Vitor","Estagiario")

    def test_presentation(self):
        expected = "Ola sou Vitor e sou um Estagiario"
        self.assertEqual(expected, self.developer.presentation())

if __name__ == '__main__':
    unittest.main()
