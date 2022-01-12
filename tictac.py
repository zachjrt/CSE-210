"""
Author: Zach Thompson
"""

gamePlay= True;

def main():
    currentPlayer = "X"
    nextPlayer(currentPlayer)
    board = makeBoard()
    while (gamePlay):
        showBoard(board)
        chooseSpot(currentPlayer, board)
        currentPlayer = nextPlayer(currentPlayer)
    
def makeBoard():
    board = []
    for spot in range(9):
        board.append(spot + 1)
    return board

def showBoard(board):   
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-----')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-----')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    
def chooseSpot(currentPlayer, board):
    spot = int(input(f"{currentPlayer}'s turn to choose a square [1-9]: "))
    board[spot - 1] = currentPlayer
    checkGame(board)

def nextPlayer(currentPlayer):
    if currentPlayer == "O":
        return "X"
    elif currentPlayer == "X":
        return "O"
    

def checkGame(board):
    if (board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or board[2] == board[4] == board[6]):
        print()
        showBoard(board)
        print("Good Game. Thanks for playing!")
        global gamePlay;
        gamePlay = False;
    else:
        gamePlay = True;

if __name__ == "__main__":
    main()