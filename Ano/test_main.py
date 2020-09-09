import unittest
from main import saberEdad

##desarrollo del text unitario
class Test(unittest.TestCase):
    def test_saber_edad(self):
        self.assertEqual(62, saberEdad(12,2020))

        if __name__ == '__main__':
            unittest.main()


