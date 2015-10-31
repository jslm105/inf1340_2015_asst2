#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"



def find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:


    In psuedo code:
    Iterate through the input string.
    If a letter matches the first letter of substring
        then check if following input_string characters are the same as substring
            print current point of iteration
    else
        return -1
    """
    for p in range(start, end):
        if substring[0] in input_string[p]:
            if substring[1:len(substring)] == input_string[p+1:p+len(substring)]:
                print p
            else:
                print -1



find("This is an example", "is", 0, 17)

def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    return result

