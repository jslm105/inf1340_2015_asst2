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

def union():
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes

    Check that each schema has same number of columns.
    Check that cell of row 1, column 1 of table 1 has the same value (in this case a string "Number" but it could be anything just so long as they're both the same) as cell of row 1, column 1 of table 2.
    Check that cell of row 1, column 2 of table 1 has the same value ("Surname") as cell of row 1, column 2 of table 2.
    Check that cell of row 1, column 3 of table 1 has the same value ("Age") as cell of row 1, column 3 of table 2.
        If all are the same then proceed with rest of function.
            Else return MismatchedAttributesException

    Rest of function:
    Check row 2 of table 2 against all rows of table 1.
        If unique append to new table called merged_table.
    Check row 3 of table 2 against all rows of table 1.
        If unique append to merged_table.
    Keep going and going (as I'm sure you can guess we'll use a loop to manage this)
    """

    # Check that schema has same number of columns
    table1_columns = len(table1[0][:])
    if len(table1[0][:]) == len(table2[0][:]):
        print ("The tables have the same number of columns")

        for same_schema in range(table1_columns):
            if table1[0][same_schema] == table2[0][same_schema]:
                print ("The column values are equal")

                #This utilizes the remove duplicate function below, need to change it to just calling the function
                #I believe this is the expected output for the union of Graduate and Managers table
                d = {}
                result = []
                for row in table3:
                    if tuple(row) not in d:
                        result.append(row)
                        d[tuple(row)] = True
                        break
                        index = 0
                        for data_set in table3:
                            union = table3[index][:]
                            print(union)
                            index += 1
                            break
                break
            else:
                print("The column values are not equal...MismatchedAttributesException")
                break

    #print table1
    #print len(table1[0][:])


    return []
union()

def intersection(table1, table2):
    """
    Perform the intersection set operation on tables, table1 and table2.

    Checks all rows found in the first table against lists(rows) in the second table
     -If the same row if found in both table1 and table2, display it
     -If a row in found only in one table and not the other, do not display it

    """
    #Displays the rows that are in both table1 and table2.
    for row in table1:
        if row in table1 and row in table2:
            print(row)

    return []


def difference(table1, table2):
    """
    Describe your function

    """
    return []


#####################
# HELPER FUNCTIONS ##
#####################


def remove_duplicates():
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """
    listy = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38],
            [7432, "O'Malley", 39]]
    d = {}
    result = []
    for row in table3:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    print result
remove_duplicates()

class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

