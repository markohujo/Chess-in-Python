from typing import List

import numpy as np

from src.board.board import Board
from src.moves.base import AMove
from src.utils.enums.color import Color
from src.pieces.base import APiece
from src.utils.enums.piece_type import PieceType


class Bishop(APiece):

    def available_moves_from(self, board: Board, x: int, y: int) -> List[AMove]:
        moves = self.moves_in(board, x, y, lambda n: n + 1, lambda n: n + 1)
        moves += self.moves_in(board, x, y, lambda n: n + 1, lambda n: n - 1)
        moves += self.moves_in(board, x, y, lambda n: n - 1, lambda n: n + 1)
        return moves + self.moves_in(board, x, y, lambda n: n - 1, lambda n: n - 1)

    def get_values(self) -> np.array:
        return np.array([
            [-20, -10, -10, -10, -10, -10, -10, -20],
            [-10,   0,   0,   0,   0,   0,   0, -10],
            [-10,   0,   5,  10,  10,   5,   0, -10],
            [-10,   5,   5,  10,  10,   5,   5, -10],
            [-10,   0,  10,  10,  10,  10,   0, -10],
            [-10,  10,  10,  10,  10,  10,  10, -10],
            [-10,   5,   0,   0,   0,   0,   5, -10],
            [-20, -10, -10, -10, -10, -10, -10, -20]
        ])

    def type(self) -> PieceType:
        return PieceType.BISHOP

    def __repr__(self) -> str:
        return "wB" if self.color == Color.WHITE else "bB"
