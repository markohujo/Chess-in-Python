from typing import List

import numpy as np

from src.board.board import Board
from src.moves.base import AMove
from src.utils.enums.color import Color
from src.pieces.base import APiece
from src.pieces.bishop import Bishop
from src.pieces.rook import Rook
from src.utils.enums.piece_type import PieceType


class Queen(APiece):

    def available_moves_from(self, board: Board, x: int, y: int) -> List[AMove]:
        moves = Rook(self.color).available_moves_from(board, x, y)
        return moves + Bishop(self.color).available_moves_from(board, x, y)

    def get_values(self) -> np.array:
        return np.array([
            [-20, -10, -10, -5, -5, -10, -10, -20],
            [-10, 0,   0,   0,  0,  0,   0,   -10],
            [-10, 0,   5,   5,  5,  5,   0,   -10],
            [-5,  0,   5,   5,  5,  5,   0,   -5],
            [0,   0,   5,   5,  5,  5,   0,   -5],
            [-10, 5,   5,   5,  5,  5,   0,   -10],
            [-10, 0,   5,   0,  0,  0,   0,   -10],
            [-20, -10, -10, -5, -5, -10, -10, -20]
        ])

    def type(self) -> PieceType:
        return PieceType.QUEEN

    def __repr__(self) -> str:
        return "wQ" if self.color == Color.WHITE else "bQ"
