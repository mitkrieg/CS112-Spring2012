#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

# Step 1:
# -----------------------
# Program the following.
# 
#    $ python prissybot.py
#    Enter your name:  Paul
#   
#    PrissyBot: Hello there, Paul
#    Paul: hi bot
#    PrissyBot: You mean, "hi bot, sir!"
# 
# Make sure the user inputs their own name and responses.

#Prissy Bot Dialouge
prissy = "Prissy Bot: "
name = raw_input("Enter your name: ")

print "%s Hello there, %s" %(prissy,name)
response = raw_input("%s: " % name)

print "You mean, \"Hi Bot, Sir!!\""
response = raw_input("%s: " % name)

print "How rude. Next time be sure to address me correctly!"
response = raw_input("%s: " % name)

#reads user input as string
print "You forgot \"Sir!\" As punishment answer this math problem: What does 4*343 equal?"
responseNumber = raw_input("%s: " % name)

if responseNumber == "1372":
    print "What took you so long? Are you Stupid?"
else:
    print "Wrong, 4*343 = ", 4*343, "You need to get your brain checked out for mental issues....."

response = raw_input("%s:" % name)
print "Whatever, now let's get down to business. I'm getting bored. Enter 5 numbers between 1 and 255 and then I will confuse you by finding the mean and then turn each number into their hexidecimal and binary form."
num1 = int(raw_input("First number: "))
num2 = int(raw_input("Second number: "))
num3 = int(raw_input("Third number: "))
num4 = int(raw_input("Fourth number: "))
num5 = int(raw_input("Fifth number: "))

# creates table with 5 numbers given by user and converts them to binary and hexidecimal
print """
Prissy Bot:
Mean: %d
Decimal (Base10)     Binary (Base 2)    Hexidecimal (Base 16)""" % ((num1+num2+num3+num4+num5)/5)
print "   %7s%19s%24s" % (num1, bin(num1), hex(num1))
print "   %7s%19s%24s" % (num2, bin(num2), hex(num2))
print "   %7s%19s%24s" % (num3, bin(num3), hex(num3))
print "   %7s%19s%24s" % (num4, bin(num4), hex(num4))
print "   %7s%19s%24s" % (num5, bin(num5), hex(num5))

print "\nDo you understand? Or are you a complete imbecile?"
response6=raw_input("%s: " % name)

print "To be honest I don't care. While you were typing to me I was thinking about better things I can do with my time. For example, I could be reducing fractions. Give me a numerator and a denominator."
numerator=int(raw_input("Numerator: "))
denominator=int(raw_input("Denominator: "))

remainindex=255
endloop=0
nummod=0
denmod=0

#Tests for the least common denominator to reduce by.
while endloop != 1:
    nummod=numerator%remainindex
    denmod=denominator%remainindex
    if nummod == 0 and denmod == 0:
        endloop=1
        numreduce = numerator/remainindex
        denreduce = denominator/remainindex
    remainindex-=1

#prints fraction
print "The fraction %d/%d reduces to %d/%d" % (numerator, denominator, numreduce, denreduce)

print "\n\nWell this has been......interesting, I'm gonna go do something else. I'll leave you with this piece of ascii art because I'm sure your little mind will stare at it for hours on end. Bye." 
response=raw_input("%s: " % name)

print """

        .;''-.
      .' |    `._
     /`  ;       `'.
   .'     \         \
  ,'\|    `|         |
  | -'_     \ `'.__,J
 ;'   `.     `'.__.'
 |      `"-.___ ,'
 '-,           /
 |.-`-.______-|
 }      __.--'L
 ;   _,-  _.-"`\         ___
 `7-;"   '  _,,--._  ,-'`__ `.
  |/      ,'-     .7'.-"--.7 |        _.-'
  ;     ,'      .' .'  .-. \/       .'
   ;   /       / .'.-     ` |__   .'
    \ |      .' /  |    \_)-   `'/   _.-'``
     _,.--../ .'     \_) '`_      \'`
   '`f-'``'.`\;;'    ''`  '-`      |
      \`.__. ;;;,   )              /
       `-._,|;;;,, /\            ,'
        / /<_;;;;'   `-._    _,-'
       | '- /;;;;;,      `t'` \. I like nonsence.
       `'-'`_.|,';;;,      '._/| It wakes up the brain cells!
       ,_.-'  \ |;;;;;    `-._/
             / `;\ |;;;,  `"     - Theodor Seuss Geisel -
           .'     `'`\;;, /
          '           ;;;'|
              .--.    ;.:`\    _.--,
             |    `'./;' _ '_.'     |
              \_     `"7f `)       /
              |`   _.-'`t-'`"-.,__.'
              `'-'`/;;  | |   \ mx
                  ;;;  ,' |    `
                      /   ' 
"""

# Step 2:
# -----------------------
# Keep adding to the conversation. Make sure that your program 
# includes the following:
# 
#  * get and use input from the user
#  * 3 math problems
#     * at least one should get numbers from the user
#  * at least 3 insults


# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4

