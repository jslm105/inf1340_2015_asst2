#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Jessica Mallender, Jake Miller & Susan Sim'
__email__ = "jessica.mallender@mail.utoronto.ca, jacob.miller@mail.utoronto.ca, ses@drsusansim.org"
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
    # Iterate through input string
    for p in range(start, end):
        # Find first letter of substring
        if substring[0] in input_string[p]:
            # Confirm remainder of substring follows in input string
            if substring[1:len(substring)] == input_string[p+1:p+len(substring)]:
                return p
                # Stop the loop at first instance
                break
            else:
                return -1



#find("This is an ex-parrot", "parrot", 0, 20)


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
        # Find first letter of substring
        if substring[0] in input_string[char]:
            # Confirm remainder of substring follows in input string
            if substring[1:len(substring)] == input_string[char+1:char+len(substring)]:
                # Compile into a string separated by commas
                result = result + "," + str(char)

            else:
                return result
    # Return string without first comma
    return result[1:]
#multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 14)
