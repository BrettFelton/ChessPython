from pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, is_white):
        self.value = 1
        self.is_white = is_white
        self.is_first_move = True

    def validate_move(self, start_position, end_position):
        rank_distance = int(end_position[1]) - int(start_position[1])
        forward_step = 1 if self.is_white else -1

        if start_position[0] != end_position[0]:
            print("Pawn can only move in its given file")
            return False
        
        if self.is_first_move:
            if rank_distance not in (forward_step, 2 * forward_step):
                print("Pawn can only move one or two spaces forward on the first turn")
                return False
            self.is_first_move = False
        else:
            if rank_distance != forward_step:
                print("Pawn can only move one space forward after its first turn")
                return False
        
        return True    

    def draw_piece(self):
        if self.is_white:
            return("♟")
        else:
            return("♙")