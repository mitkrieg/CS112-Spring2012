#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

def greeter(name):
    if type(name) is int:
        print "hello,", name
    else:
        print "hello,", name.lower()


# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

def box(w,h):
    if type(w) is int and type(h) is int:
        if w == 1 and h == 1:
            print "+"
        elif w ==1 and h == 2:
            print "+\n+"
        elif w == 2 and h == 1:
            print "++"
        elif w > 1 and h > 1:
            print "+" + "-"*(w-2) + "+"
            for i in range(h-2):
                print "|" + " "*(w-2) + "|"
            print "+" + "-"*(w-2) + "+"
        else:
           print "Error: Invalid Dimensions" 
    else:
        print "Error: Invalid Dimensions"



# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

#def tree((*rows,*trunk),*star,*leaf,*ornament):
#return " "*rows