#!/usr/bin/env python

from exercise2 import find, multi_find

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Jessica Mallender, Jake Miller & Susan Sim'
__email__ = "jessica.mallender@mail.utoronto.ca, jake.miller@mail.utoronto.ca, ses@drsusansim.org"
__copyright__ = "2015 Mallender, Miller & Sim"
__license__ = "MIT License"


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14
    assert find("This is an ex-parrot", "is", 0, 20) == 2
    assert find("This is an ex-parrot", "parbot", 0, 20) == -1
    assert find("And now for something completely different", "completely", 0, 42) == 22
    assert find("And now for something completely different", "om", 0, 42) == 13
    assert find("And now for something completely different", "lumberjack", 0, 42) == -1
    assert find("I'm a lumberjack and I'm OK", "OK", 0, 26) == 25
    assert find("I'm a lumberjack and I'm OK", "I'm", 0, 26) == 0
    assert find("I'm a lumberjack and I'm OK", "parrot", 0, 26) == -1


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"
    assert multi_find("Ni! Ni! Ni! Ni!", "i", 0, 20) == "1,5,9,13"
    assert multi_find("Ni! Ni! Ni! Ni!", "No", 0, 20) == ""
    assert multi_find("I'm a lumberjack and I'm OK. I'm a lumberjack and I'm OK.", "OK", 0, 57) == "25,54"
    assert multi_find("I'm a lumberjack and I'm OK. I'm a lumberjack and I'm OK.", "lumber", 0, 57) == "6,35"
    assert multi_find("I'm a lumberjack and I'm OK. I'm a lumberjack and I'm OK.", "parrot", 0, 57) == ""
    assert multi_find("It's just a flesh wound", "s", 0, 22) == "3,7,15"
    assert multi_find("It's just a flesh wound", "flesh", 0, 22) == "12"
    assert multi_find("It's just a flesh wound", "knight", 0, 22) == ""
