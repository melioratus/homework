Rock Paper Scissors Game
========================

What are the rules?
-------------------

-   Player can pick
    
    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    </colgroup>
    <thead>
    <tr>
    <th scope="col" class="org-left">Choices</th>
    </tr>
    </thead>
    
    <tbody>
    <tr>
    <td class="org-left">Rock</td>
    </tr>
    
    
    <tr>
    <td class="org-left">Paper</td>
    </tr>
    
    
    <tr>
    <td class="org-left">Scissors</td>
    </tr>
    </tbody>
    </table>
    
    -   Rock beats Scissors
    
    -   Scissors beats Paper
    
    -   Paper beats Rock

-   Game is 3 rounds
    
        #
        # Start
        #
        r=3
        
        i=0

-   2 people to play
    
        #
        # Ask Player 1 to choose rock paper or scissors
        #
        
        player1 = raw_input('Player 1, choose rock, paper or scissors: ')
    
        #
        # Ask Player 2 to choose rock paper or scissors
        #
        
        player2 = raw_input('Player 2, choose rock, paper or scissors: ')

How do we know which player wins?
---------------------------------

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Player 1</th>
<th scope="col" class="org-left">Player 2</th>
<th scope="col" class="org-left">Winner</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Rock</td>
<td class="org-left">Rock</td>
<td class="org-left">Tie</td>
</tr>


<tr>
<td class="org-left">Paper</td>
<td class="org-left">Paper</td>
<td class="org-left">Tie</td>
</tr>


<tr>
<td class="org-left">Scissors</td>
<td class="org-left">Scissor</td>
<td class="org-left">Tie</td>
</tr>


<tr>
<td class="org-left">Rock</td>
<td class="org-left">Scissor</td>
<td class="org-left">Player 1</td>
</tr>


<tr>
<td class="org-left">Rock</td>
<td class="org-left">Paper</td>
<td class="org-left">Player 2</td>
</tr>


<tr>
<td class="org-left">Paper</td>
<td class="org-left">Rock</td>
<td class="org-left">Player 1</td>
</tr>


<tr>
<td class="org-left">Paper</td>
<td class="org-left">Scissor</td>
<td class="org-left">Player 2</td>
</tr>


<tr>
<td class="org-left">Scissors</td>
<td class="org-left">Paper</td>
<td class="org-left">Player 1</td>
</tr>


<tr>
<td class="org-left">Scissors</td>
<td class="org-left">Rock</td>
<td class="org-left">Player 2</td>
</tr>
</tbody>
</table>

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
    # Check & Say Winner
    #
    
    print checkwinner(player1,player2)

Rock Paper Scissors Program
===========================

Below is the [rock-paper-scissors](rock-paper-scissors.py) program

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
