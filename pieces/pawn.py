from pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, is_white):
        self.value = 1
        self.is_white = is_white

    def valid_move(self):
        pass    

    def draw_piece(self):
        if self.is_white:
            return("♟")
        else:
            return("♙")