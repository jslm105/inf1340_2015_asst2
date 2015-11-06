#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Jessica Mallender, Jake Miller & Susan Sim'
__email__ = "jessica.mallender@mail.utoronto.ca, jake.miller@mail.utoronto.ca, ses@drsusansim.org"
__copyright__ = "2015 Mallender, Miller & Sim"
__license__ = "MIT License"


vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
latinify_vowel = "yay"
latinify_consonant = "ay"


def pig_latinify(word):
    """
    This function takes an English word and translates it into Pig Latin.
    This version of Pig Latin is based off of the following rules:
    -If the word starts with a vowel, append "yay" to the end of the word
    -If the word starts with a consonant, every consonant up to the first
     vowel is removed and appended to the end. Finally "ay" is appended to
     the end as well.
    -Non- English arguments are returned in its as-is form

    :param : word: an English word (string)
    :return: English word translated into Pig Latin (string) or non-English argument returned as entered

    """ 

    result = " "

    # Piglainifys word that starts with a vowel
    if word[0] in vowels:
        result = word + latinify_vowel

    # Piglatinfys a word that starts with a consonant
    elif word[0] in consonants:
        for vowel_position in range(1, len(word)):
            if word[vowel_position] in vowels:
                result = (word[vowel_position:] + word[:vowel_position] + latinify_consonant)
                break
            else:
                result = word + latinify_consonant

    # Returns the word if it is not a standard English word
    else:
        result = word

    return result
