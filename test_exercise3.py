#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS
Test module for exercise3.py
"""

from exercise3 import union, intersection, difference, check_schema, MismatchedAttributesException

__author__ = 'Jessica Mallender, Jake Miller & Susan Sim'
__email__ = "jessica.mallender@mail.utoronto.ca, jake.miller@mail.utoronto.ca, ses@drsusansim.org"
__copyright__ = "2015 Mallender, Miller & Sim"
__license__ = "MIT License"


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

STUDENTS = [["Number", "Surname", "Age", "Degree"],
            [7274, "Robinson", 37, "MI"],
            [7432, "O'Malley", 39, "MI"],
            [9824, "Darkes", 38, "MI"]]

PROFESSORS = [["ID Number", "Surname", "Age"],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

INSTRUCTORS = [["ID Number", "Surname", "Age"],
               [9297, "O'Malley", 56],
               [7432, "O'Malley", 39],
               [9824, "Darkes", 38]]


#####################
# HELPER FUNCTIONS ##
#####################

def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################

def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))


def test_union_none():
    """
    Test union operation on identical tables.
    """
    result = [["ID Number", "Surname", "Age"],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(PROFESSORS, INSTRUCTORS))


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))


def test_intersection_none():
    """
    Test intersection operation on identical tables.
    """
    result = [["ID Number", "Surname", "Age"],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(PROFESSORS, INSTRUCTORS))


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))


def test_difference_none():
    """
    Test difference operation on identical tables.
    """
    result = [['ID Number', 'Surname', 'Age']]

    assert is_equal(result, difference(PROFESSORS, INSTRUCTORS))
#####################
# REMOVE DUPLICATES##
#####################


def test_remove_duplicates():
    """
    Test duplicates are removed.
    """
    result_union = [[7274, "Robinson", 37],
                    [7432, "O'Malley", 39],
                    [9297, "O'Malley", 56],
                    [9824, "Darkes", 38],
                    ["Number", "Surname", "Age"]]

    result_intersection = [[7432, "O'Malley", 39],
                           [9824, "Darkes", 38],
                           ["Number", "Surname", "Age"]]

    result_difference = [[7274, "Robinson", 37],
                         ["Number", "Surname", "Age"]]

    assert result_union == sorted(union(GRADUATES, MANAGERS))
    assert result_intersection == sorted(intersection(GRADUATES, MANAGERS))
    assert result_difference == sorted(difference(GRADUATES, MANAGERS))


##########################
# SCHEMA CHECK FUNCTION ##
##########################

def test_schema_check():
    """
    Tests to make sure that our check_schema helper function raises the
    MismatchedAttributesException if the two tables column numbers or
    values are different
    """
    # Tables have different number of columns
    try:
        check_schema(GRADUATES, STUDENTS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    # Tables have different column values
    try:
        check_schema(GRADUATES, PROFESSORS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    # Tables have different number of columns and values
    try:
        check_schema(PROFESSORS, STUDENTS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

#######################
# NEGATIVE TEST CASES##
#######################

# Negative test cases for union function


def test_union_negative():
    """
    Tests to make sure that our union function raises the
    MismatchedAttributesException if the two tables column numbers or
    values are different
    """
    # Tables have different number of columns
    try:
        union(GRADUATES, STUDENTS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    # Tables have different column values
    try:
        union(GRADUATES, PROFESSORS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    # Tables have different number of columns and values
    try:
        union(PROFESSORS, STUDENTS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

# Negative test cases for intersection function


def test_intersection_negative():
    """
    Tests to make sure that our intersection function raises the
    MismatchedAttributesException if the two tables column numbers or
    values are different
    """
    # Tables have different number of columns
    try:
        union(GRADUATES, STUDENTS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    # Tables have different column values
    try:
        union(GRADUATES, PROFESSORS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    # Tables have different number of columns and values
    try:
        union(PROFESSORS, STUDENTS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

# Negative test cases for difference function


def test_difference_negative():
    """
    Tests to make sure that our difference function raises the
    MismatchedAttributesException if the two tables column numbers or
    values are different
    """
    # Tables have different number of columns
    try:
        union(GRADUATES, STUDENTS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    # Tables have different column values
    try:
        union(GRADUATES, PROFESSORS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False

    # Tables have different number of columns and values
    try:
        union(PROFESSORS, STUDENTS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False
