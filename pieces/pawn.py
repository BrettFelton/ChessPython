from pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, is_white):
        self.value = 1
        self.is_white = is_white
        self.is_first_move = True
        self.is_en_passentable = False

    def validate_move(self, start_position, end_position):
        rank_distance = int(end_position[1]) - int(start_position[1])
        forward_step = 1 if self.is_white else -1

        if start_position[0] != end_position[0]:
            print("Pawn can only move in its given file")
            return False
        
        if self.is_first_move:
            if rank_distance == (2 * forward_step):
                is_en_passentable = True
            if rank_distance not in (forward_step, 2 * forward_step):
                print("Pawn can only move one or two spaces forward on the first turn")
                return False
            self.is_first_move = False
        else:
            is_en_passentable = False
            if rank_distance != forward_step:
                print("Pawn can only move one space forward after its first turn")
                return False

        #TODO: pawns are the only pieces that take diagonally. Need to figure out that logic here.
        #TODO: pawns can also take on en passent. Need to figure out that logic here or somewhere else aswell. 

        return True    

    def draw_piece(self):
        if self.is_white:
            return("♟")
        else:
            return("♙")