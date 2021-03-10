
import unittest
import functions

"""
Reference : https://docs.python.org/3/library/unittest.html
"""
class TestClass(unittest.TestCase):
    def setUp(self):
        print("set up")

    #@unittest.skip("demonstrating skipping")
    def test_multiplication(self):
        self.assertEqual(functions.multiply(3,3), 9, "should be 9")

    def tearDown(self):
        print("tear down")

if __name__ == '__main__':
    unittest.main()