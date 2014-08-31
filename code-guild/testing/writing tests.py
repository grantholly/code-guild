__author__ = 'grant'


def similarity(set1, set2):
    intersection = 0.0

    for element in set1:
        if element in set2:
            intersection += 1

    union = len(set1) + len(set2) - intersection

    return intersection / union


print(similarity(['a', 'b'], ['b', 'c', 'd']))

print(similarity(['a', 'a'], ['a', 'b']))

"""
This is buggy.  We have an intersection of 'a', but we are counting
the non-distinct elements for 'a' giving us a total intersection of 2.
Then when we calculate the union, we see that 4.  Our quotient of
the intersection and union then returns 2/2 which is 1.
"""


def improved_similarity(set1, set2):
    set1 = set(set1)
    set2 = set(set2)

    intersection = set1.intersection(set2)

    union = set1.union(set2)

    #if not union:
    #    return 0/0

    return float(len(intersection)) / float(len(union))
    #this is to avoid the from __future__ import division for
    #floating point division defaults in Python 3.x


print(improved_similarity(['a', 'b'], ['b', 'c', 'd']))

print(improved_similarity(['a', 'a'], ['a', 'b']))


#from myapplication import improved_similarity

#test two sets with an intersection
assert(improved_similarity(['a', 'b'], ['b', 'c', 'd'])) == 0.25
#test two sets with non-distinct elements
assert(improved_similarity(['a', 'a'], ['a', 'b'])) == 0.5
#test two sets with no intersection
assert(improved_similarity(['a', 'b'], ['c', 'd', 'e'])) == 0.0

"""
If this test was hit before the others, the program will terminate early
with an error.
"""

#assert(improved_similarity([], [])) == 0.0
assert(improved_similarity(['a', 'b'], ['b', 'c', 'd'])) == 0.25
assert(improved_similarity(['a', 'a'], ['a', 'b'])) == 0.5
assert(improved_similarity(['a', 'b'], ['c', 'd', 'e'])) == 0.0


def test_sets_with_intersection():
    assert(improved_similarity(['a', 'b'], ['b', 'c', 'd'])) == 0.25


def test_sets_with_non_distinct_elements():
    assert(improved_similarity(['a', 'a'], ['a', 'b'])) == 0.5


def test_sets_with_empty_sets():
    assert(improved_similarity([], [])) == 0.0


def test_sets_with_no_intersection():
    assert(improved_similarity(['a', 'b'], ['c', 'd', 'e'])) == 0.0


if __name__ == '__main__':
    for test in [test_sets_with_intersection,
                 test_sets_with_non_distinct_elements,
                 test_sets_with_empty_sets,
                 test_sets_with_no_intersection]:
        try:
            test
        except Exception as e:
            print("!!!{} FAILED: {}!!!".format(test.__name__, e))
        else:
            print("{} PASSED".format(test.__name__))








