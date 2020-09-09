import unittest
from main import saberPalabra
##Test

class Test(unittest.TestCase):
        def test_saber_palabra(self):
            self.assertEqual("ar",saberPalabra("amor"))
if __name__ == '__main__':
          unittest.main()
