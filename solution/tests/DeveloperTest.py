import unittest
from models.Developer import Developer

class DeveloperTestCase(unittest.TestCase):
    def setUp(self):
        self.developer = Developer("Vitor","Estagiario")

    def test_presentation(self):
        expected = "Name: vitor Experience: estagiario"
        self.assertEqual(expected, self.developer.presentation())

if __name__ == '__main__':
    unittest.main()
