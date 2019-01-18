"""Unit test of get.py"""
import unittest
import get
from pprint import pprint

class TestWebParser(unittest.TestCase):

    def test_get_problem(self):
        wp = get.WebParser()
        p = wp.get_problem(1)
        pprint(vars(p))



if __name__ == '__main__':
    unittest.main()

