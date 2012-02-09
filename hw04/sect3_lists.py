#!/usr/bin/env python
from hwtools import *

print "Section 3:  Lists"
print "-----------------------------"

nums = input_nums()
# 1. "nums" is a list of numbers entered from the command line.  How many
#    numbers were entered?

length=len(nums)
print "1.", length

# 2.  Append 3 and 5 to nums
nums.append(3)
nums.append(5)
print "2.", nums

# 3.  Remove the last element from nums

nums.pop(len(nums)-1)
print "3.", nums


# 4.  Set the 3rd element to 7

nums[2]=7
print "4.", nums


# 5. [ADVANCED] Grab a new list of numbers and add it to the existing one

nums2=input_nums()
nums += nums2
print "5.", nums


# 6. [ADVANCED] Make a copy of this new giant list and delete the 2nd 
#    through 4th values

nums_copy = nums[:]
for i in range (1,4):
    nums_copy.pop(1)
print "6.", nums,"\n", nums_copy

# 7-9. [ADVANCED] Print the following:

print "7.", nums[0:3]    # first 3 elements
print "8.", nums[len(nums)-1]    # last element

newnums = [nums[1]]
print "9.", newnums    # a list of the second element
