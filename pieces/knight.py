from pieces.piece import Piece

class Knight(Piece):
    def __init__(self, is_white):
        self.value = 3
        self.is_white = is_white

    def validate_move(self, start_position, end_position):
        file_distance = abs(ord(end_position[0]) - ord(start_position[0]))
        rank_distance = abs(int(end_position[1]) - int(start_position[1]))

        if not ((file_distance == 2 and rank_distance == 1) or (file_distance == 1 and rank_distance == 2)):
            print("Knight must move in an L-shape (2 squares in one direction, 1 in the other)")
            return False

        return True

    def draw_piece(self):
        if self.is_white:
            return("♞")
        else:
            return("♘")