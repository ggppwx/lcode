"""Unit test of get.py"""
import unittest
import get
from pprint import pprint
import shutil

class TestWebParser(unittest.TestCase):

    def test_get_problem(self):
        wp = get.WebParser()
        p = wp.get_problem(1)
        pprint(vars(p))


class TestTemplateCreator(unittest.TestCase):
    def test_create_template(self):
        test_dir = '.'
        problem = get.Problem(1, 'test', 'tst1', 'http://test')
        wp = get.TemplateCreator(test_dir)
        wp.create_template(problem)
        shutil.rmtree('1. test')



if __name__ == '__main__':
    unittest.main()

 
