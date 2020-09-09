import unittest

from main import saberAño


class Test(unittest.TestCase):
    def test_saber_año(self):
        self.assertEqual(2078,saberAño(2078))
if __name__ == '__main__':
    unittest.main()