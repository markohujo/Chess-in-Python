from typing import List

import numpy as np

from src.board.board import Board
from src.moves.base import AMove
from src.utils.enums.color import Color
from src.pieces.base import APiece
from src.utils.enums.piece_type import PieceType


class Knight(APiece):

    def available_moves_from(self, board: Board, x: int, y: int) -> List[AMove]:
        moves = []
        moves += self.move_on(board, x, y, x + 2, y + 1)
        moves += self.move_on(board, x, y, x + 2, y - 1)
        moves += self.move_on(board, x, y, x + 1, y + 2)
        moves += self.move_on(board, x, y, x + 1, y - 2)
        moves += self.move_on(board, x, y, x - 2, y + 1)
        moves += self.move_on(board, x, y, x - 2, y - 1)
        moves += self.move_on(board, x, y, x - 1, y + 2)
        moves += self.move_on(board, x, y, x - 1, y - 2)
        return moves

    def get_values(self) -> np.array:
        return np.array([
            [-50, -40, -30, -30, -30, -30, -40, -50],
            [-40, -20, 0,   0,   0,   0,   -20, -40],
            [-30, 0,   10,  15,  15,  10,  0,   -30],
            [-30, 5,   15,  20,  20,  15,  5,   -30],
            [-30, 0,   15,  20,  20,  15,  0,   -30],
            [-30, 5,   10,  15,  15,  10,  5,   -30],
            [-40, -20, 0,   5,   5,   0,   -20, -40],
            [-50, -40, -30, -30, -30, -30, -40, -50]

        ])

    def type(self) -> PieceType:
        return PieceType.KNIGHT

    def __repr__(self) -> str:
        return "wN" if self.color == Color.WHITE else "bN"
