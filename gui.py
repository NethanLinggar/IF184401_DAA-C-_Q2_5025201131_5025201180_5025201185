from functions import *
from state import *
from tkinter import *
from functools import partial
from tkinter import messagebox
import random, sys
import art

class Game(Tk):
    def __init__(self, is_user_first):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("400x400")
        self.resizable(False, False)

        self.is_user_first = is_user_first
        self.button_list = []
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.current_character = 'X'
        self.corner_pieces = [
            (0,0),(0,2),(2,0),(2,2)
        ]
        if self.is_user_first:
            self.player = 'O'
            self.opponent = 'X'
        else:
            self.player = 'X'
            self.opponent = 'O'

if __name__ == "__main__":
    is_user_first = False

    # ASCII art
    print(art.text2art("Fico", "small"))
    print(art.text2art("Gaming", "small"))

    game = Game(is_user_first=is_user_first)
    game.mainloop()