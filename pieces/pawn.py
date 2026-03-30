from pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, is_white):
        self.value = 1
        self.is_white = is_white
        self.is_first_move = True

    def validate_move(self, start_position, end_position):
        move_distance = int(end_position[1]) - int(start_position[1])

        if start_position[0] != end_position[0]:
            print("Pawn piece can only move in its given file")
            return False
        
        if self.is_first_move:
            if move_distance > 2 or move_distance <= 0:
                print("Pawn piece can only move one or two spaces on the first turn")
                return False
            self.is_first_move = False
        else:
            if move_distance > 1 or move_distance <= 0:
                print("Pawn piece can only move one space after its first turn")
                return False
        
        return True    

    def draw_piece(self):
        if self.is_white:
            return("♟")
        else:
            return("♙")