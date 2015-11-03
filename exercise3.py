#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

table1 =     [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

table2 =    [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

table3 = table1 + table2

#####################
# HELPER FUNCTIONS ##
#####################


def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """
    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result
#remove_duplicates()

def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.
    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
    """
    # Check that schema has same number of columns
    if len(table1[0]) == len(table2[0]):
        # Check that schema has same categories
        if table1[0] == table2[0]:
                #Create table of containing both tables

                table3 = table1 + table2
        else:
            raise MismatchedAttributesException
    else:
        raise MismatchedAttributesException
    #Remove all duplicates leaving one complete table
    table3 = remove_duplicates(table3)
    return table3

#union(table1, table2)

def intersection(table1, table2):
    """
    Perform the intersection set operation on tables, table1 and table2.

    Checks all rows found in the first table against lists(rows) in the second table
     -If the same row if found in both table1 and table2, it is displayed in the new intersection table
     -If a row in found only in one table and not the other, do not add it to the new table

    """
    #Displays the rows that are in both table1 and table2.

    intersection_table = []
    for row in table1:
        if row in table1 and row in table2:
            intersection_table.append(row)

    return intersection_table


def difference(table1, table2):
    """
    Perform the difference set operation on tables, table1 and table2.

    Checks all rows in table1 against rows in table2
     - If a row in table1 is not in table2, the row is displayed in the new difference table
     -If a row is in both tables do not add it to the new table


    """

    difference_table= [table1[0]]
    for row in table1:
        if row not in table2:
            difference_table.append(row)

    return difference_table




class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

