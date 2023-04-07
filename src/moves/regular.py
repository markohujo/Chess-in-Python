from abc import ABC

from src.board.board import Board
from src.moves.base import AMove
from src.squares.empty import EmptySquare
from src.squares.piece import PieceSquare


class RegularMove(AMove):
    """Represents a regular one piece move (including a regular capture move)"""

    def __init__(self, square_from, square_to, board: Board):
        super().__init__(square_from, square_to, board)
        self.square_to = square_to
        self.piece_first_move_tmp = False

    def execute(self):
        super().execute()
        self.set_first_move()
        self.board.set_square(PieceSquare(self.square_to.x, self.square_to.y, self.square_from.piece))
        self.board.set_square(EmptySquare(self.square_from.x, self.square_from.y))

    def undo(self):
        super().undo()
        self.unset_first_move()
        self.board.set_square(self.square_from)
        self.board.set_square(self.square_to)

    def castling(self):
        return False

    def set_first_move(self):
        """If this move is the first move of its piece, save this information and set the first move attribute of the piece to False"""

        if self.square_from.piece.first_move:
            self.piece_first_move_tmp = True
            self.square_from.piece.first_move = False

    def unset_first_move(self):
        """Unset this move's piece first move attribute"""

        if self.piece_first_move_tmp:
            self.square_from.piece.first_move = True
