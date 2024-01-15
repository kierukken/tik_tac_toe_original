tic_tac_toe = [["_","_","_"],["_","_","_"],["_","_","_"]]
P1P,P1P2, P2P, P2P2 = 0, 0, 0, 0
def Startgame():
    global tic_tac_toe
    tic_tac_toe = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    print("Board Cleared!")
def PrintBoard():
    for x in tic_tac_toe:
        for y in x:
            print(y, end=" ")
        print()
def Player1turn():
    global P1P, P1P2, tic_tac_toe
    PrintBoard()
    while(True):
        P1P, P1P2 = input("Player 1 where would you like to go: ").split()
        P1P, P1P2 = int(P1P), int(P1P2)
        if tic_tac_toe[P1P][P1P2] == "O":
            print("This position has already been taken! Try again.")
        else:
            tic_tac_toe[P1P][P1P2] = "X"
            break
def Player2turn():
    global P2P, P2P2, tic_tac_toe
    PrintBoard()
    while(True):
        P2P, P2P2 = input("Player 2 where would you like to go: ").split()
        P2P, P2P2 = int(P2P), int(P2P2)
        if tic_tac_toe[P2P][P2P2] == "X":
            print("This position has already been taken! Try again.")
        else:
            tic_tac_toe[P2P][P2P2] = "O"
            break
def PlayerWinCheck():
    global startinput, tic_tac_toe
    rematchinput = "0"
    i=0
    while i < 3:
        if  tic_tac_toe[i][0] == "X" and tic_tac_toe[i][1] == "X" and tic_tac_toe[i][2] == "X":
            rematchinput = input("Player 1 has won! \nWould you like to play again yes or no: ")
        elif tic_tac_toe[i][0] == "O" and tic_tac_toe[i][1] == "O" and tic_tac_toe[i][2] == "O":
            rematchinput = input("Player 2 has won! \nWould you like to play again yes or no: ")
        elif  tic_tac_toe[0][i] == "X" and tic_tac_toe[1][i] == "X" and tic_tac_toe[2][i] == "X":
            rematchinput = input("Player 1 has won! \nWould you like to play again yes or no: ")
        elif tic_tac_toe[0][i] == "O" and tic_tac_toe[1][i] == "O" and tic_tac_toe[2][i] == "O":
            rematchinput = input("Player 2 has won! \nWould you like to play again yes or no: ")
        elif tic_tac_toe[0][0] == "X" and tic_tac_toe[1][1] == "X" and tic_tac_toe[2][2] == "X" or tic_tac_toe[0][2] == "X" and tic_tac_toe[1][1] == "X" and tic_tac_toe[2][0] == "X":
            rematchinput = input("Player 1 has won! \nWould you like to play again yes or no: ")
        elif tic_tac_toe[0][0] == "O" and tic_tac_toe[1][1] == "O" and tic_tac_toe[2][2] == "O" or tic_tac_toe[0][2] == "O" and tic_tac_toe[1][1] == "O" and tic_tac_toe[2][0] == "O":
            rematchinput = input("Player 2 has won! \nWould you like to play again yes or no: ")
        return rematchinput
        i = i+1
def playgame():
    while(True):
        Player1turn()
        rematch = PlayerWinCheck()
        if rematch == "yes" or rematch == "Yes":
            return rematch
            break
        elif len(rematch) > 1:
            return rematch
            break
        Player2turn()
        rematch = PlayerWinCheck()
        if rematch == "yes" or rematch == "Yes":
            return rematch
            break
        elif len(rematch) > 1:
            break
startinput = input("would you like to start the game print Yes or No: ")
while(True):
    if startinput == "Yes" or startinput == "yes":
        break
    elif startinput == "No" or startinput == "no":
        startinput = input("print yes when you would like the play: ")
    else:
        startinput = input("please print Yes or No: ")
while(True):
    Startgame()
    x = playgame()
    if x.lower() != "yes":
        break