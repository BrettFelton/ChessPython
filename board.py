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
        self.init_white_pieces()
        self.init_black_pieces() 

    def build_board(self):
        result = {}
        for file in files:
            for rank in ranks:
                result[f"{file}{rank}"] = None
        return result


    def init_white_pieces(self):
        self.board[f"a1"] = Rook(True) 
        self.board[f"b1"] = Knight(True)
        self.board[f"c1"] = Bishop(True)
        self.board[f"e1"] = King(True)
        self.board[f"d1"] = Queen(True)
        self.board[f"e1"] = Bishop(True)
        self.board[f"f1"] = Knight(True)
        self.board[f"h1"] = Rook(True)
        for file in files:
            self.board[f"{file}{2}"] = Pawn(True)
            for rank in ranks:
                if rank in ("3", "5"):
                    if file in ("b", "d", "f", "h"):
                        self.board[f"{file}{rank}"] = Space(True)
                if rank in ("4", "6"):
                    if file in ("a", "c", "e", "g"):
                        self.board[f"{file}{rank}"] = Space(True)

    def init_black_pieces(self):
        self.board[f"a8"] = Rook(True) 
        self.board[f"b8"] = Knight(True)
        self.board[f"c8"] = Bishop(True)
        self.board[f"e8"] = King(False)
        self.board[f"d8"] = Queen(False)
        self.board[f"e8"] = Bishop(True)
        self.board[f"f8"] = Knight(True)
        self.board[f"h8"] = Rook(True)
        for file in files:
            self.board[f"{file}{7}"] = Pawn(False)
            for rank in ranks:
                if rank in ("3", "5"):
                    if file in ("a", "c", "e", "g"):
                        self.board[f"{file}{rank}"] = Space(False)
                if rank in ("4", "6"):
                    if file in ("b", "d", "f", "h"):
                        self.board[f"{file}{rank}"] = Space(False)

    def draw_board(self):
        result = []
        for rank in ranks:
            file_view = f"{rank}"            
            for file in files:
                current_field = self.board[f"{file}{rank}"]
                # Draw empty board spaces
                if not current_field:
                    file_view += "_"
                #     if rank in ("3", "5"):
                #         if file in ("A", "C", "E", "G"):
                #             file_view += "□"
                #         else:
                #             file_view += "■"
                #     elif rank in ("4", "6"):
                #         if file in ("A", "C", "E", "G"):
                #             file_view += "■"
                #         else:
                #             file_view += "□"
                # Draw pieces on board
                else:
                    file_view += current_field.draw_piece()
            result.append(file_view)
        result.append(" abcdefgh")

        for row in result:
            print(row)
