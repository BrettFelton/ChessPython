from pieces.piece import Piece
from pieces.space import Space
from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.pawn import Pawn

ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
files = ["a", "b", "c", "d", "e", "f", "g", "h"]

class Board():
    def __init__(self):
        self.board = self.build_board()
        self.init_pieces(True, 1, 2)
        self.init_pieces(False, 8, 7)

    def build_board(self):
        result = {}
        for file in files:
            for rank in ranks:
                result[f"{file}{rank}"] = None
        return result

    def init_pieces(self, is_white, main_rank, pawn_rank):
        # Main row pieces
        self.board[f"a{main_rank}"] = Rook(is_white) 
        self.board[f"b{main_rank}"] = Knight(is_white)
        self.board[f"c{main_rank}"] = Bishop(is_white)
        self.board[f"d{main_rank}"] = Queen(is_white)
        self.board[f"e{main_rank}"] = King(is_white)
        self.board[f"f{main_rank}"] = Bishop(is_white)
        self.board[f"g{main_rank}"] = Knight(is_white)
        self.board[f"h{main_rank}"] = Rook(is_white)
        
        # Pawn pieces
        for file in files:
            self.board[f"{file}{pawn_rank}"] = Pawn(is_white)

        # Open space pieces
        rank1 = ranks[2:6:2]
        rank2 = ranks[3:7:2]
        if is_white:
            file1 = files[1::2]
            file2 = files[::2]
        else:
            file1 = files[::2]
            file2 = files[1::2]

        for rank in rank1:
            for file in file1:
                self.board[f"{file}{rank}"] = Space(is_white)
        for rank in rank2:
            for file in file2:
                self.board[f"{file}{rank}"] = Space(is_white)

    def draw_board(self):
        result = []
        for rank in ranks:
            file_view = f"{rank}"            
            for file in files:
                current_field = self.board[f"{file}{rank}"]
                # Draw pieces on board
                if current_field:
                    file_view += current_field.draw_piece()
                # Draw empty board spaces
                else:
                    file_view += "_"
            result.append(file_view)
        result.append(" abcdefgh")

        for row in result:
            print(row)
