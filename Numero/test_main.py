import unittest
from main import saberTipo
##test
class Test(unittest.TestCase):
    def test_saber_tipo(self):
        self.assertEqual(1, saberTipo(True))
        if __name__ == '__main__':
            unittest.main()

