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

    """
    x=0
    for p in range(start,end):
        if substring in input_string[p]:
                print(p)

    return -1

find("This is an example", "i", 0, 17)

def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    return result

