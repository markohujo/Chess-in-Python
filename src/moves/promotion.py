from abc import ABC

from src.board.board import Board
from src.moves.base import AMove
from src.pieces.queen import Queen
from src.squares.empty import EmptySquare
from src.squares.piece import PieceSquare


class Promotion(AMove):
    """Represents a pawn promotion"""

    def __init__(self, square_from, square_to, board: Board):
        super().__init__(square_from, square_to, board)
        self.promoted_piece = Queen(self.square_from.piece.color)

    def execute(self):
        super().execute()
        self.board.set_square(PieceSquare(self.square_to.x, self.square_to.y, self.promoted_piece))
        self.board.set_square(EmptySquare(self.square_from.x, self.square_from.y))

    def undo(self):
        super().undo()
        self.board.set_square(self.square_from)
        self.board.set_square(self.square_to)

    def castling(self):
        return False

    def set_promoted_piece(self, piece):
        self.promoted_piece = piece
