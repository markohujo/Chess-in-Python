import operator

from src.board.board import Board
from src.moves.castling.base import ACastling
from src.squares.piece import PieceSquare


class LongCastling(ACastling):
    """Represents a long castling move"""

    def __init__(self, square_from: PieceSquare, board: Board):
        super().__init__(square_from,
                         board.at(square_from.x, square_from.y - 2),
                         board.at(square_from.x, square_from.y - 4),
                         operator.sub,
                         board)

    def execute(self):
        super().execute()

    def undo(self):
        super().undo()
