#!/usr/bin/env python3

from checkmate import  condition_game

def main(): 

    board = [
        "R...",
        ".K..",
        "..P.",
        "...."
        ]



    condition_game(board)

if __name__ == "__main__":
    main()
