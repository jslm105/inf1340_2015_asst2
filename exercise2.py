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
    Find the index position of the first instance of the substring in input_string.

    :param : input_string: a long string
    :param : substring: a short string
    :param : start: first index position of input_string
    :param : end: last index position of input_string
    :return: index position, -1 if not found
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
        return -1
    # Return only first instance
    else:
        return result[0]


def multi_find(input_string, substring, start, end):
    """
    Find all index positions of the substring in input_string.

    :param : input_string: a long string
    :param : substring: a short string
    :param : start: first index position of input_string
    :param : end: last index position of input_string
    :return: index position(s), empty string if not found
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
