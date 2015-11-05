#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Jessica Mallender, Jake Miller & Susan Sim'
__email__ = "jessica.mallender@mail.utoronto.ca, jacob.miller@mail.utoronto.ca, ses@drsusansim.org"
__copyright__ = "2015 Mallender, Miller & Sim"
__license__ = "MIT License"



from exercise1 import pig_latinify


def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

def test_no_vowels():
    """
    Test case tests for words that contain no vowels

    """
    assert pig_latinify("rhythm") == "rhythmay"

def test_empty_string():
    """
    Test case tests to make sure function returns an empty string as an empty string
    :return:
    """
    assert pig_latinify(" ") == " "

def test_numbers():
    """
    Test case tests to make sure function does not Piglatinfy numbers

    """
    assert pig_latinify("123456") == "123456"



