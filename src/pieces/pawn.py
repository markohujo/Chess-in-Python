import operator
from typing import List

import numpy as np

from src.board.board import Board
from src.moves.base import AMove
from src.moves.en_passant import EnPassant
from src.moves.promotion import Promotion
from src.utils.enums.color import Color
from src.moves.regular import RegularMove
from src.pieces.base import APiece
from src.utils.enums.piece_type import PieceType


class Pawn(APiece):

    def available_moves_from(self, board: Board, x: int, y: int) -> List[AMove]:
        if self.color == Color.WHITE:
            return self.__generate_moves(board, x, y, operator.sub)
        return self.__generate_moves(board, x, y, operator.add)

    def get_values(self) -> np.array:
        return np.array([
            [0,  0,  0,   0,   0,   0,   0,  0],
            [50, 50, 50,  50,  50,  50,  50, 50],
            [10, 10, 20,  30,  30,  20,  10, 1],
            [5,  5,  10,  25,  25,  10,  5,  5],
            [0,  0,  0,   20,  20,  0,   0,  0],
            [5,  -5, -10, 0,   0,   -10, -5, 5],
            [5,  10, 10,  -20, -20, 10,  10, 5],
            [0,  0,  0,   0,   0,   0,   0,  0]
        ])

    def __generate_moves(self, board: Board, x: int, y: int, color_op: operator) -> List[AMove]:
        return self.__generate_regular_moves(board, x, y, color_op) + \
               self.__generate_capture_moves(board, x, y, color_op)

    def __generate_regular_moves(self, board: Board, x: int, y: int, color_op: operator) -> List[AMove]:
        moves = []

        x1 = color_op(x, 1)
        x2 = color_op(x, 2)

        if self.first_move and board.empty_at(x1, y) and board.empty_at(x2, y):
            moves.append(RegularMove(board.at(x, y), board.at(x2, y), board))

        if board.empty_at(x1, y):
            if x1 == 0 or x1 == 7:
                moves.append(Promotion(board.at(x, y), board.at(x1, y), board))
            else:
                moves.append(RegularMove(board.at(x, y), board.at(x1, y), board))

        return moves

    def __generate_capture_moves(self, board: Board, x: int, y: int, color_op: operator) -> List[AMove]:
        moves: List[AMove] = []

        x1 = color_op(x, 1)
        left_square = board.at(x1, y - 1)
        right_square = board.at(x1, y + 1)

        if left_square.enemy(self.color):
            if x1 == 0 or x1 == 7:
                moves.append(Promotion(board.at(x, y), left_square, board))
            else:
                moves.append(RegularMove(board.at(x, y), left_square, board))

        if right_square.enemy(self.color):
            if x1 == 0 or x1 == 7:
                moves.append(Promotion(board.at(x, y), right_square, board))
            else:
                moves.append(RegularMove(board.at(x, y), right_square, board))

        return moves + self.__en_passant(board, x, y, color_op)

    def __en_passant(self, board: Board, x: int, y: int, color_op: operator) -> List[EnPassant]:
        moves = self.__en_passant_direction(board, x, y, color_op, operator.add)
        return moves + self.__en_passant_direction(board, x, y, color_op, operator.sub)

    def __en_passant_direction(self, board: Board, x: int, y: int, color_op: operator, direction_op: operator):
        x_cmp = 3 if self.color == Color.WHITE else 4

        if x == x_cmp and \
                board.empty_at(color_op(x, 1), direction_op(y, 1)) and \
                board.last_move.match(color_op(x, 2), direction_op(y, 1), x, direction_op(y, 1)) and \
                not board.empty_at(x, direction_op(y, 1)) and \
                board.piece_at(x, direction_op(y, 1)).type() == PieceType.PAWN:
            return [EnPassant(board.at(x, y),
                              board.at(color_op(x, 1), direction_op(y, 1)),
                              board.at(x, direction_op(y, 1)),
                              board)]

        return []

    def type(self) -> PieceType:
        return PieceType.PAWN

    def __repr__(self) -> str:
        return "wp" if self.color == Color.WHITE else "bp"
