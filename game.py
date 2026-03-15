from board import Board

class Game():
    def __init__(self):
        self.board = Board()
        self.new_game()

    def new_game(self):
        print("New Game Started")
        print("Here is the board")
        self.board.draw_board()
