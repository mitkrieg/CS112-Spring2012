#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
import hwtools
from hwtools import input_nums

nums=input_nums()
sortnums=sorted(nums)
print "I have sorted your numbers"
print sortnums
x=int(raw_input("Which number should I find: "))
m=0
M=len(sortnums)-1
while M>=m:
    md=int((M+m)/2)
    if sortnums[md]==x:
        break
    elif sortnums[md]<=x:
       m=md+1
    elif sortnums[md]>x:
        M=md-1
if sortnums[md]==x:
    print "Found", x, "at", md
else:
    print "Could not find", x
print sortnums
