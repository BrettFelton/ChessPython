from pieces.piece import Piece

class King(Piece):
    def __init__(self, is_white):
        self.value = None
        self.is_white = is_white

    def validate_move(self, start_position, end_position):
        pass    

    def draw_piece(self):
        if self.is_white:
            return("♚")
        else:
            return("♔")