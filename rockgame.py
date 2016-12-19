# ***********************************************************
# Author - Harshit Prasad
# Date - 19.12.2016
# Rock-Paper-Scissor
while True:
    player1 = input('Player 1 enter your choice -')
    player2 = input('Player 2 enter your choice -')
    if player1==player2:
        print('TIE')
    else:
        if player1=='rock' and player2=='scissor':
            print('player1 won!')
        elif player1=='rock' and player2=='paper':
            print('player2 won!')
        elif player1 == 'paper' and player2 =='scissor':
            print('player2 won!')
        elif player1 == 'paper' and player2 == 'rock':
            print('player1 won!')
        elif player1 == 'scissor' and player2 == 'rock':
            print('player2 won!')
        elif player1 == 'scissor' and player2 == 'paper':
            print('player1 won!')
        else:
            pass
    restart = input('Do you want to restart the game again?')
    x = 'YES'
    y = 'NO'
    if restart == x:
        continue
    else:
        break