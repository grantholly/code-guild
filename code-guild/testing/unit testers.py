__author__ = 'grant'

#pip install pytest
#pip install nose (nosetests)

from file_to_test import functions_to_test
from unittest import TestCase


def test_sets_with_intersection():
    assert(improved_similarity(['a', 'b'], ['b', 'c', 'd'])) == 0.25


def test_sets_with_non_distinct_elements():
    assert(improved_similarity(['a', 'a'], ['a', 'b'])) == 0.5


def test_sets_with_empty_sets():
    assert(improved_similarity([], [])) == 0.0


def test_sets_with_no_intersection():
    assert(improved_similarity(['a', 'b'], ['c', 'd', 'e'])) == 0.0

"""
pytest (http://pytest.org/latest/)
looks for any function with the prefix of test_*
and runs it as a test and exports the test results
run your test with >>>py.test then your file.py

 $ py.test test_assert1.py
 =========================== test session starts ============================
 platform linux -- Python 3.4.0 -- py-1.4.23 -- pytest-2.6.1
 collected 1 items

 test_assert1.py F

 ================================= FAILURES =================================
 ______________________________ test_function _______________________________

     def test_function():
 >       assert f() == 4
 E       assert 3 == 4
 E        +  where 3 = f()

 test_assert1.py:5: AssertionError
 ========================= 1 failed in 0.01 seconds =========================
"""


class TestImprovedSimilarity(TestCase):
    def test_sets_with_intersection():
        my_test = improved_similarity(['a', 'b'], ['b', 'c', 'd'])
        self.assertEqual(my_test, 0.25)

    def test_sets_with_non_distinct_elements():
        my_test = test_sets_with_non_distinct_elements(['a', 'a'], ['a', 'b'])
        self.assertEqual(my_test, 0.5)

    def test_sets_with_empty_sets():
        my_test = improved_similarity([], [])
        self.assertEqual(my_test, 0.0)

    def test_sets_with_no_intersection():
        my_test = test_sets_with_no_intersection(['a', 'b'], ['c', 'd', 'e'])
        self.assertEqual(my_test, 0.0)