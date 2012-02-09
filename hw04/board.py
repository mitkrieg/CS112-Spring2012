#!/usr/bin/env python
#This program makes an ascii checerboard based on a user inputted width and length.

print "Let's make a checkerboard!"
width = int(raw_input("Enter a width: "))
length = int(raw_input("Enter a length: "))
print " "
test = 1

while test % length > 0:
    if test % 2 == 1:
        for x in range (0,width):
            if x % 2 == 1:
                print "#",
            else:
                print "-",
    else:
        for y in range (0,width):
            if y % 2 == 1:
                print "-",
            else:
                print "#",
    print ""
    test += 1

#must draw one extra line to compensate for the stop
if test % 2 == 1:
    for x in range (0,width):
        if x % 2 == 1:
            print "#",
        else:
            print "-",
else:
    for y in range (0,width):
        if y % 2 == 1:
            print "-",
        else:
            print "#",
print "\nTa-Da!"
            
