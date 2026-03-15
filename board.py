from pieces.piece import Piece
from pieces.space import Space
from pieces.pawn import Pawn

ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
files = ["A", "B", "C", "D", "E", "F", "G", "H"]

class Board():
    def __init__(self):
        self.board = self.build_board()
        self.init_white_pieces()
        self.init_black_pieces() 

    def build_board(self):
        result = {}
        for file in files:
            for rank in ranks:
                result[f"{file} + {rank}"] = None
        return result


    def init_white_pieces(self):
        for file in files:
            self.board[f"{file} + {2}"] = Pawn(True)
            for rank in ranks:
                if rank in ("3", "5"):
                    if file in ("B", "D", "F", "H"):
                        self.board[f"{file} + {rank}"] = Space(True)
                if rank in ("4", "6"):
                    if file in ("A", "C", "E", "G"):
                        self.board[f"{file} + {rank}"] = Space(True)


    def init_black_pieces(self):
        pieces = []
        for file in files:
            self.board[f"{file} + {7}"] = Pawn(False)
            for rank in ranks:
                if rank in ("3", "5"):
                    if file in ("A", "C", "E", "G"):
                        self.board[f"{file} + {rank}"] = Space(False)
                if rank in ("4", "6"):
                    if file in ("B", "D", "F", "H"):
                        self.board[f"{file} + {rank}"] = Space(False)

    def draw_board(self):
        result = []
        for rank in ranks:
            file_view = f"{rank}"            
            for file in files:
                current_field = self.board[f"{file} + {rank}"]
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
        result.append(" ABCDEFGH")

        for row in result:
            print(row)
