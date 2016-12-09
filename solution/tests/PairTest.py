import unittest
from models.Developer import Developer
from models.Pair import Pair

class PairTestCase(unittest.TestCase):
    def setUp(self):
        self.developer1 = Developer("Vitor" , "Estagiario")
        self.developer2 = Developer("Lucas" , "Pleno")

        self.pair = Pair(self.developer1 , self.developer2)

    def test_presentation(self):
        expected = "Driver: Vitor - Navigator: Lucas"
        self.assertEqual(expected, self.pair.presentation())

if __name__ == '__main__':
    unittest.main()
