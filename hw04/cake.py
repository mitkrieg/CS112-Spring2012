#!/usr/bin/env python

#A program version of [cake or death] (http://youtu.be/BNjcuZ-LiSY)

playing = True
cake = 3

while playing:
    answer = raw_input("Cake or Death? ")
    if answer == "Cake" or answer == "cake":
        if cake > 2:
            print "Here is a pice of Triple Chocolate Truffle Cake!"
            cake -= 1
        elif cake > 1:
            print "Here is a piece of Ice Cream Cake!"
            cake -= 1
        elif cake > 0:
            print "Here is a piece of Black Forrest Cake"
            cake -= 1
        else:
            print "I'm sorry we are out of cake. I apologize for any inconvience."
    elif answer == "Death" or answer == "death":
        print "It was a bright and sunny day in the middle of the month of May and you were walking along the beach with your significant other. Suddenly a giant unicorn lands in front of you and declares that you will die a horrible death in 30 minutes. The next 30 minutes is the greatest half hour of your life. Then a woman appears standing waste deep in the water. You walk out to her. She reachers her hand out and touches your chest. She wispers, \"You're it.\" and you fall backward into utter bliss and die."
        playing = False
