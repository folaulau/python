
import unittest
import functions
from tests import TestClass

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestClass('test_multiplication'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())