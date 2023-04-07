import numpy as np

from src.board.board import Board
from src.utils.enums.color import Color
from src.pieces.bishop import Bishop
from src.pieces.king import King
from src.pieces.knight import Knight
from src.pieces.pawn import Pawn
from src.pieces.queen import Queen
from src.pieces.rook import Rook
from src.squares.empty import EmptySquare
from src.squares.piece import PieceSquare


class BoardFactory:
    """Factory for creating chessboards"""

    @staticmethod
    def create() -> Board:
        """Create a new chessboard"""

        return Board(np.array([
            [PieceSquare(0, 0, Rook(Color.BLACK)), PieceSquare(0, 1, Knight(Color.BLACK)),
             PieceSquare(0, 2, Bishop(Color.BLACK)), PieceSquare(0, 3, Queen(Color.BLACK)),
             PieceSquare(0, 4, King(Color.BLACK)), PieceSquare(0, 5, Bishop(Color.BLACK)),
             PieceSquare(0, 6, Knight(Color.BLACK)), PieceSquare(0, 7, Rook(Color.BLACK))],
            [PieceSquare(1, 0, Pawn(Color.BLACK)), PieceSquare(1, 1, Pawn(Color.BLACK)),
             PieceSquare(1, 2, Pawn(Color.BLACK)), PieceSquare(1, 3, Pawn(Color.BLACK)),
             PieceSquare(1, 4, Pawn(Color.BLACK)), PieceSquare(1, 5, Pawn(Color.BLACK)),
             PieceSquare(1, 6, Pawn(Color.BLACK)), PieceSquare(1, 7, Pawn(Color.BLACK))],
            [EmptySquare(2, 0), EmptySquare(2, 1), EmptySquare(2, 2), EmptySquare(2, 3),
             EmptySquare(2, 4), EmptySquare(2, 5), EmptySquare(2, 6), EmptySquare(2, 7)],
            [EmptySquare(3, 0), EmptySquare(3, 1), EmptySquare(3, 2), EmptySquare(3, 3),
             EmptySquare(3, 4), EmptySquare(3, 5), EmptySquare(3, 6), EmptySquare(3, 7)],
            [EmptySquare(4, 0), EmptySquare(4, 1), EmptySquare(4, 2), EmptySquare(4, 3),
             EmptySquare(4, 4), EmptySquare(4, 5), EmptySquare(4, 6), EmptySquare(4, 7)],
            [EmptySquare(5, 0), EmptySquare(5, 1), EmptySquare(5, 2), EmptySquare(5, 3),
             EmptySquare(5, 4), EmptySquare(5, 5), EmptySquare(5, 6), EmptySquare(5, 7)],
            [PieceSquare(6, 0, Pawn(Color.WHITE)), PieceSquare(6, 1, Pawn(Color.WHITE)),
             PieceSquare(6, 2, Pawn(Color.WHITE)), PieceSquare(6, 3, Pawn(Color.WHITE)),
             PieceSquare(6, 4, Pawn(Color.WHITE)), PieceSquare(6, 5, Pawn(Color.WHITE)),
             PieceSquare(6, 6, Pawn(Color.WHITE)), PieceSquare(6, 7, Pawn(Color.WHITE))],
            [PieceSquare(7, 0, Rook(Color.WHITE)), PieceSquare(7, 1, Knight(Color.WHITE)),
             PieceSquare(7, 2, Bishop(Color.WHITE)), PieceSquare(7, 3, Queen(Color.WHITE)),
             PieceSquare(7, 4, King(Color.WHITE)), PieceSquare(7, 5, Bishop(Color.WHITE)),
             PieceSquare(7, 6, Knight(Color.WHITE)), PieceSquare(7, 7, Rook(Color.WHITE))]
        ]))
