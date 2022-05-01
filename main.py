from tokenize import Number
# from gui import *
from state import *
from functions import *

startState = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

maxPlayer, minPlayer = 'X', 'O'
bestScore = 0

def main():
    boardState = State(startState, None, 0, None, maxPlayer)


    print('Welcome to the program! Please enter an index')
    boardState.printState()

    MIndex = input()
    MIndex = int(MIndex)

    boardState = enterInIndex(boardState, MIndex)
    boardState = findBestMove(boardState)

    while not isGameOver(boardState):
        boardState.printState()
        print('Please enter another index')
        MIndex = input()
        MIndex = int(MIndex)
        boardState = enterInIndex(boardState, MIndex)
        boardState = findBestMove(boardState)

    print('Game Over!')
    boardState.printState()
    return


if __name__ == "__main__":
    main()