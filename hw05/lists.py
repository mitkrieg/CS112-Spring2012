#!/usr/bin/env python
import math
"""lists.py

A bunch of excercises to see if you understand list comprehensions
"""

import os

# Solve the following problems with one python statement.  It is fine 
# to break up the statement into multiple lines as long as it is only
# one actual command.
#
# This is fine:
#   print [ (x,y) 
#           for x in range(10)
#           for y in range(10) ]
#

# 1. Read a bunch of numbers from the input separated by spaces and 
#    convert them to ints


print "1.", [int(x) for x 
             in raw_input("Enter in numbers separated by spaces: ").split()]

# 2.  Read another bunch of numbers, convert them, and return the list 
#     of only the first 3
print "2.", [int(x) for x 
             in raw_input("Enter in numbers separated by spaces: ").split()
             ][0:3]

# 3.  Read a bunch of words separated by commas from the command line,
#     remove any excess spaces, and print a list of their lenghts
print "3.", [len(word.strip()) for word 
            in raw_input("Enter words separated by commas: ").split(",")]

# 4.  Create a list of every multiple of 3 between 1 and 100 with their 
#     index
#        ex:  [ [0,3], [1,6], [2,9]...]
print "4.", [[y/3-1,y] 
             for y in range(1,101)
             if y % 3 == 0
             ]

# 5. create a list of every card in a deck of cards 
print "5.", [[suit, card]
             for card in "Ace", 2,3,4,5,6,7,8,9,10, "Jack", "Queen", "King"
             for suit in 'Diamonds', 'Hearts', 'Spades', 'Clubs'
             ]

# 6.  Create a 5 by 5 array filled with zeros
print "6.", [[0 for colum in range(5)]for row in range(5)]


# 7.  Make a list of every perfect square between 1 and 1000
print "7.", [q**2 for q in range(101) if q**2 <= 1000]

# 8.  Make a list of every perfect square between 1 and 1000 
#     a different way
print "8.", [w**2
             for w in range(int(math.sqrt(32**2)))]

# 9.  List every python file in this directory
print "9.", [pyfile for pyfile in  os.listdir(os.getcwd())
             if pyfile.split(".")[-1] == "py"]

# 10.  Print a list of every pythagorean triple with a side less than
#      or equal to 20.  Don't include duplicates ([3,4,5] == [4,3,5])
print "10.",[[x,y,z]
         for x in range (1,21)
         for y in range (1,21)
         for z in range (1,21)
         if x**2 + y**2 == z**2 and x <= y and y <=z]



# I couldn't in good concious include this, but it is fun to 
# figure out/find.

## NOT REQUIRED
# 11.  Print a list of every prime number less than 100
#print "11.", []


