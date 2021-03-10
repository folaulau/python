
import unittest
import functions

class TestClass(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(functions.multiply(3,3), 9, "should be 9")


if __name__ == '__main__':
    unittest.main()