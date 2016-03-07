#!/usr/bin/env python
#
# Start
#
r=3

i=0


def checkwinner(p1,p2):
    if p1 == p2:
        return 'Tie'
    elif p1 == 'rock'     and p2 == 'scissors':
        return 'Player 1 wins!'
    elif p1 == 'rock'     and p2 == 'paper':
        return 'Player 2 wins!'
    elif p1 == 'paper'    and p2 == 'rock':
        return 'Player 1 wins!'
    elif p1 == 'paper'    and p2 == 'scissors':
        return 'Player 2 wins!'
    elif p1 == 'scissors' and p2 == 'paper':
        return 'Player 1 wins!'
    elif p1 == 'scissors' and p2 == 'rock':
        return 'Player 2 wins!'
    else:
        return 'Uh oh! I cannot tell who won the game!'


#
# Loop
#

while i < r:

    #
    # Ask Player 1 to choose rock paper or scissors
    #
    
    player1 = raw_input('Player 1, choose rock, paper or scissors: ')

    #
    # Ask Player 2 to choose rock paper or scissors
    #
    
    player2 = raw_input('Player 2, choose rock, paper or scissors: ')

    #
    # Check & Say Winner
    #
    
    print checkwinner(player1,player2)

    #
    # i+1
    #
    i = i + 1


#
# Stop
#
