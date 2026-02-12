#!/usr/bin/env python3

from checkmate import  condition_game

def main(): 

    board_str = """\
        R...
        .K..
        ..P.
        ....\
        """

    condition_game(board_str)

if __name__ == "__main__":
    main()
