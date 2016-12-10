import unittest
import settings
from models.Developer import Developer

class DeveloperTestCase(unittest.TestCase):
    def setUp(self):
        self.developer = Developer("Vitor",1)
        ops = ['Estagiario' , 'Junior' , 'Pleno' , 'Senior']
        options = settings.setOptions(ops)

    def test_presentation(self):
        expected = "Name: Vitor Experience: Estagiario"
        self.assertEqual(expected, self.developer.presentation())

if __name__ == '__main__':
    unittest.main()
