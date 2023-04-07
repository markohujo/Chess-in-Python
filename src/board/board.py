from typing import List

import numpy as np

from src.squares.piece import PieceSquare
from src.utils.color_converter import ColorConverter
from src.utils.enums.color import Color
from src.squares.base import ASquare
from src.squares.offboard import OffBoardSquare
from src.utils.enums.piece_type import PieceType


class Board:
    """Represents a chess board, that is 8*8 grid of squares (empty or with pieces)"""

    def __init__(self, square_grid: np.array) -> None:
        self.square_grid = square_grid
        self.last_move = None

    def generate_possible_moves(self, color: Color) -> list:
        """Returns list containing all valid moves for all pieces of the given color"""

        moves = []

        for piece_square in self.piece_squares(color):
            moves += piece_square.piece.valid_moves(self, piece_square.x, piece_square.y)

        return moves

    def calc_value(self, color: Color) -> int:
        """Calculate value of the board for the given color

        https://en.wikipedia.org/wiki/Chess_piece_relative_value
        """

        value = 0

        for piece_square in self.piece_squares(color):
            value += piece_square.piece.get_value_at(piece_square.x, piece_square.y)

        for enemy_square in self.piece_squares(ColorConverter.convert(color)):
            value -= enemy_square.piece.get_value_at(enemy_square.x, enemy_square.y)

        return value

    def valid_move(self, move, color: Color) -> bool:
        """Return True if the given move is valid, False otherwise

        Move is valid if it does not result in check
        """

        move.execute()
        check = self.check(color)
        move.undo()

        return not check

    def check(self, color: Color) -> bool:
        """Return True if the given color is in check, False otherwise"""

        for enemy_piece in self.piece_squares(ColorConverter.convert(color)):
            for move in enemy_piece.piece.available_moves_from(self, enemy_piece.x, enemy_piece.y):
                if not move.square_to.empty() and move.square_to.piece.type() == PieceType.KING:
                    return True

        return False

    def checkmate(self, color: Color) -> bool:
        """Return True if the given color is in checkmate, False otherwise

        Player is in checkmate if its king is in danger and cannot move
        """

        return self.check(color) and len(self.generate_possible_moves(color)) == 0

    def stalemate(self, color: Color) -> bool:
        """ Return True if the given color is in stalemate, False otherwise

        Player is in stalemate if it cannot move
        """

        return len(self.generate_possible_moves(color)) == 0

    def piece_squares(self, color: Color) -> List[PieceSquare]:
        """Return piece squares of the given color"""

        res = []

        for row in self.square_grid:
            for elem in row:
                if not elem.empty() and elem.piece.color == color:
                    res.append(elem)

        return res

    def short_castle_possible(self, x: int, y: int):
        """Return True if king can castle (short castling) from [x,y] square, False otherwise"""

        return self.empty_at(x, y + 1) and \
            self.empty_at(x, y + 2) and \
            not self.empty_at(x, y + 3) and \
            self.piece_at(x, y + 3).type() == PieceType.ROOK and \
            self.piece_at(x, y + 3).first_move

    def long_castle_possible(self, x: int, y: int):
        """Return True if king can castle (long castling) from [x,y] square, False otherwise"""

        return self.empty_at(x, y - 1) and \
            self.empty_at(x, y - 2) and \
            self.empty_at(x, y - 3) and \
            not self.empty_at(x, y - 4) and \
            self.piece_at(x, y - 4).type() == PieceType.ROOK and \
            self.piece_at(x, y - 4).first_move

    def set_square(self, square: ASquare) -> None:
        """Sets the given square in this board"""
        self.square_grid[square.x, square.y] = square

    def empty_at(self, x: int, y: int) -> bool:
        """Return True if square at the given coordinates is empty, False otherwise"""
        return self.at(x, y).empty()

    def enemy_at(self, x: int, y: int, color: Color) -> bool:
        """Return True if square at the given coordinates contains an enemy piece, False otherwise"""
        return self.at(x, y).enemy(color)

    def piece_at(self, x: int, y: int):
        """Return piece at the given coordinates"""
        return self.at(x, y).piece

    def at(self, x: int, y: int):
        """Return square at the given coordinates"""
        return self.square_grid[x, y] if self.__valid_coordinates(x, y) else OffBoardSquare()

    @staticmethod
    def __valid_coordinates(x: int, y: int) -> bool:
        """Return True if the given coordinates are valid, False otherwise"""
        return x in range(0, 8) and y in range(0, 8)

    def __str__(self):
        return str(self.square_grid)
