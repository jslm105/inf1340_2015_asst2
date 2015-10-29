#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    return result


vowels = ("aeiouAEIOU")
consonants = ("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
latinify_vowel = "yay"
latinify_consonants = "ay"


def pig_latinify (word):
    result = ""

    if word[0] in vowels:
        result = word + latinify_vowel


    elif word[0] in consonants:
        for vowel_position in range(1, len(word)):
            if word[vowel_position] in vowels:
                result = (word[vowel_position:] + word[:vowel_position] + latinify_consonants)
                break
    else:
        result = ("Invalid character")

    return result



pig_latin_word = pig_latinify("science")
print(pig_latin_word)
