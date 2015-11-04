#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Jessica Mallender & Jake Miller'
__email__ = ""
__copyright__ = "2015 Mallender, Miller & Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    This function takes an English word and translates it into Pig Latin.
    This version of Pig Latin is based off of the following rules:
    -If the word starts with a vowel, append "yay" to the end of the word
    -If the word starts with a consonant, every consonant up to the first
     vowel is removed and appended to the end. Finally "ay" is appended to
     the end as well.

    :param : word: an English word(string)
    :return: word translated into Piglatin (string)
    :raises:

    """ 

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
                result = word + latinify_consonants

    else:
        result = word

    return result



pig_latin_word = pig_latinify("9987897")
print(pig_latin_word)



#questions:
#1) can we assume only lowercase
#2) can we assume only one word
#3) if there is a number or different character in word do we have to account for this
# or assume that everything is ok
