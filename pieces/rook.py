from pieces.piece import Piece

# Castle
class Rook(Piece):
    def __init__(self, is_white):
        self.value = 5
        self.is_white = is_white

    def validate_move(self, start_position, end_position):
        pass    

    def draw_piece(self):
        if self.is_white:
            return("♜")
        else:
            return("♖")