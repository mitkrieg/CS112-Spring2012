#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
total = 0
# 1. What is the sum of all the numbers in nums?
for i in range(0,len(nums)):
    total += nums[i]
print "1.", total, "\n"


# 2. Print every even number in nums
print "2. even numbers:"
for a in range (0,len(nums)):
    if nums[a] % 2 == 0:
        print nums[a]
print ""
#CODE GOES HERE


# 3. Does nums only contain even numbers? 

only_even=True
for x in range (0,len(nums)):
    if nums[x] % 2 == 1:
        only_even = False

print "3.",
if only_even == True:
    print "only even"
else:
    print "some odd"
print ""

# 4. Generate a list every odd number less than 100. Hint: use range()
odds=[]
for odd in range (1,100,2):
    odds.append(odd)

print "4.", odds, "\n"

# 5. [ADVANCED]  Multiply each element in nums by its index
for z in range (0,len(nums)):
    nums[z] *= z
print "5.", nums
