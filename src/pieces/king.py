from typing import List

import numpy as np

from src.board.board import Board
from src.moves.base import AMove
from src.utils.enums.color import Color
from src.moves.castling.long import LongCastling
from src.moves.castling.short import ShortCastling
from src.pieces.base import APiece
from src.utils.enums.piece_type import PieceType


class King(APiece):

    def available_moves_from(self, board: Board, x: int, y: int) -> List[AMove]:
        moves: List[AMove] = []

        if self.first_move and board.short_castle_possible(x, y):
            moves.append(ShortCastling(board.at(x, y), board))

        if self.first_move and board.long_castle_possible(x, y):
            moves.append(LongCastling(board.at(x, y), board))

        moves += self.move_on(board, x, y, x, y + 1)
        moves += self.move_on(board, x, y, x, y - 1)
        moves += self.move_on(board, x, y, x + 1, y + 1)
        moves += self.move_on(board, x, y, x + 1, y - 1)
        moves += self.move_on(board, x, y, x + 1, y)
        moves += self.move_on(board, x, y, x - 1, y)
        moves += self.move_on(board, x, y, x - 1, y + 1)
        return moves + self.move_on(board, x, y, x - 1, y - 1)

    def get_values(self) -> np.array:
        return np.array([
            [-20, -10, -10, -10, -10, -10, -10, -20],
            [-10,   0,   0,   0,   0,   0,   0, -10],
            [-10,   0,   5,  10,  10,   5,   0, -10],
            [-10,   5,   5,  10,  10,   5,   5, -10],
            [-10,   0,  10,  10,  10,  10,   0, -10],
            [-10,  10,  10,  10,  10,  10,  10, -10],
            [-10,   5,   0,   0,   0,   0,   5, -10],
            [-20, -10, -10, -10, -10, -10, -10, -20],
        ])

    def type(self) -> PieceType:
        return PieceType.KING

    def __repr__(self) -> str:
        return "wK" if self.color == Color.WHITE else "bK"
