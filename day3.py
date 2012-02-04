#!/usr/bin/env python

print "Hello... I'm sorry you are?"
name=raw_input()
print "Hello, ",name

print "Enter words to put in pig latin"
word=raw_input()
outword=word[1:]+word[0]+"ay"
print word, "in pig latin is ",outword
