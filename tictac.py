"""
Author: Zach Thompson
"""

def main():
    currentPlayer = "none"
    board = makeBoard()
    gamePlay = true;
    while (gamePlay):
        showBoard(board)
    
def makeBoard():
    board = []
    for spot in range(9):
        board.append(spot + 1)
    return board

def showBoard():   
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-----')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-----')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    
def chooseSpot():
    spot = int(input(f"{currentPlayer}'s turn to choose a square [1-9]: "))
    board[spot - 1] = currentPlayer

def nextPlayer(currentPlayer):
    if currentPlayer == "none" or currentPlayer == "O":
        currentPlayer == "X";
    elif currentPlayer == "X":
        currentPlayer == "O"
    return currentPlayer
    

if __name__ == "__main__":
    main()