#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Jessica Mallender, Jake Miller & Susan Sim'
__email__ = "jessica.mallender@mail.utoronto.ca, jake.miller@mail.utoronto.ca, ses@drsusansim.org"
__copyright__ = "2015 Mallender, Miller & Sim"
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
    result = []
    # Iterate through input string
    for char in range(start, end):
        # Find instances of substring
        if substring[0:len(substring)] in input_string[char:char + len(substring)]:
            # Add to list if instance found
            result.append(char)
    # If substring not found
    if not result:
        print -1
    # Return only first instance
    else:
        print result[0]


def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""
    # Iterate through input string
    for char in range(start, end):
        # Find instances of substring
        if substring[0:len(substring)] in input_string[char:char + len(substring)]:
            # Compile into a string separated by commas
            result = result + "," + str(char)
    # Return string without first comma
    return result[1:]
# multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 14)
