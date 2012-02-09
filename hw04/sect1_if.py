#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

if n % 2 == 0:
    answer="even"
else:
    answer="odd"

print "1.", answer


# 2. If n is odd, double it
if answer == "odd":
    n *= 2

print "2.", n


# 3. If n is evenly divisible by 3, add four
if n % 3 == 0:
    n += 4

print "3.", n


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

while grade <= 0 or grade >= 100:
    grade = raw_input("Enter a grade [0-100]: ")
    grade = int(grade)

if grade >= 97:
    letter = "A+"
elif grade >= 93:
    letter = "A"
elif grade >= 90:
    letter = "A-"
if grade >= 87:
    letter = "B+"
elif grade >= 83:
    letter = "B"
elif grade >= 80:
    letter = "B-"
if grade >= 77:
    letter = "C+"
elif grade >= 73:
    letter = "C"
elif grade >= 70:
    letter = "C-"
if grade >= 67:
    letter = "D+"
elif grade >= 63:
    letter = "D-"
else:
    letter = "F"

print "4.", letter

