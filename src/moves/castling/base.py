import operator
from abc import ABC

from src.board.board import Board
from src.moves.base import AMove
from src.squares.empty import EmptySquare
from src.squares.piece import PieceSquare


class ACastling(AMove, ABC):
    """Represents a castling move"""

    def __init__(self,
                 square_from: PieceSquare,
                 square_to: EmptySquare,
                 rook_square: PieceSquare,
                 op: operator,
                 board: Board):
        super().__init__(square_from, square_to, board)
        self.rook_square = rook_square
        self.op = op

    def execute(self) -> None:
        super().execute()

        self.board.set_square(PieceSquare(self.square_from.x, self.op(self.square_from.y, 1), self.rook_square.piece))
        self.board.set_square(PieceSquare(self.square_from.x, self.op(self.square_from.y, 2), self.square_from.piece))

        self.board.set_square(EmptySquare(self.square_from.x, self.square_from.y))
        self.board.set_square(EmptySquare(self.rook_square.x, self.rook_square.y))

        self.square_from.piece.first_move = False
        self.rook_square.piece.first_move = False

    def undo(self) -> None:
        super().undo()

        self.square_from.piece.first_move = True
        self.rook_square.piece.first_move = True

        self.board.set_square(self.square_from)
        self.board.set_square(self.rook_square)

        self.board.set_square(EmptySquare(self.square_from.x, self.op(self.square_from.y, 1)))
        self.board.set_square(EmptySquare(self.square_from.x, self.op(self.square_from.y, 2)))

    def castling(self):
        return True
