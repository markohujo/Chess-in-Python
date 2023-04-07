from abc import ABC, abstractmethod
from typing import Optional, List, Callable

import numpy as np

from src.board.board import Board
from src.moves.base import AMove
from src.utils import board_values
from src.utils.enums.color import Color
from src.moves.regular import RegularMove
from src.utils.enums.piece_type import PieceType


class APiece(ABC):
    """
    Abstract class representing each chess piece
    """

    def __init__(self, color: Color) -> None:
        self.color = color
        self.first_move = True

    @abstractmethod
    def available_moves_from(self, board: Board, x: int, y: int) -> List[AMove]:
        """Return all available moves that this piece can do"""

    def valid_move_to(self, board: Board, x: int, y: int, x_to: int, y_to: int) -> Optional[AMove]:
        """Return this piece's move to dest if it is a valid move or None if it is invalid"""

        for move in self.valid_moves(board, x, y):
            if move.square_to.x == x_to and move.square_to.y == y_to:
                return move

        return None

    def valid_moves(self, board: Board, x: int, y: int) -> List[AMove]:
        """Return list of all valid moves of this piece at the given square

        Move is valid if it does not result in check
        """

        valid_moves = []

        for move in self.available_moves_from(board, x, y):
            if board.valid_move(move, self.color):
                valid_moves.append(move)

        return valid_moves

    def moves_in(self, board: Board, x: int, y: int, fx: Callable, fy: Callable) -> List[AMove]:
        """Return a list containing all moves from [x,y] in the given direction"""

        moves = []

        x_to = fx(x)
        y_to = fy(y)

        while board.empty_at(x_to, y_to):
            moves.append(RegularMove(board.at(x, y), board.at(x_to, y_to), board))
            x_to = fx(x_to)
            y_to = fy(y_to)

        if board.enemy_at(x_to, y_to, self.color):
            moves.append(RegularMove(board.at(x, y), board.at(x_to, y_to), board))

        return moves

    def move_on(self, board: Board, x_from: int, y_from: int, x_to: int, y_to: int) -> List[AMove]:
        """Return list containing move of this piece from [x_from, y_from] to [x_to, y_to] if the destination square is empty or occupied by an enemy piece, empty list otherwise"""

        if board.empty_at(x_to, y_to):
            return [RegularMove(board.at(x_from, y_from), board.at(x_to, y_to), board)]

        if board.enemy_at(x_to, y_to, self.color):
            return [RegularMove(board.at(x_from, y_from), board.at(x_to, y_to), board)]

        return []

    def get_value_at(self, x: int, y: int) -> int:
        """Return value of this piece at the given square"""

        value = board_values.values[self.type()]
        x = x if self.color == Color.WHITE else 7 - x
        value += self.get_values()[x, y]
        return value

    @abstractmethod
    def get_values(self) -> np.array:
        """Return numpy 2D array representing relative piece values for this piece"""

    @abstractmethod
    def type(self) -> PieceType:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
