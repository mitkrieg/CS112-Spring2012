#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

print "------NIMS------"

playing = True
game = True
player = 1

#Start Game
while playing:
    #Gets initial conditions from user
    stones = int(raw_input("Number of stones in pile: "))
    maxstones = int(raw_input("Maximum number of stones per turn: "))
    while maxstones > stones:
        print "Maximum cannot be higher that number in pile!!!"
        maxstones = int(raw_input("Maximum number of stones per turn: "))

    print "\nLet's play nims!\n"
    game = True

    #player's turn
    while game:
        turn = int(raw_input("%02d stones left. Player %d [1-%d]: "
                             % (stones,player,maxstones)))
        while turn <= 0 or turn > stones or turn > maxstones:
            print "Invalid number of stones. Try Again."
            turn = int(raw_input("%02d stones left. Player %d [1-%d]: " 
                                 % (stones,player,maxstones)))

        stones -= turn

        #Changes who's turn it is
        if player == 1:
            player = 2
        elif player == 2:
            player = 1

        #Ends game/Restarts game based on user input
        if stones == 0:
            print "Player",player,"wins!!!!\n"
            again = raw_input("Play again? ")
            again = again.lower().strip()
            if again == "no":
                game = False
                playing = False
                print "Bye!"
            if again == "yes":
                game = False
                print ""
    
