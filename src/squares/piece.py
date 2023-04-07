from src.utils.enums.color import Color
from src.squares.base import ASquare


class PieceSquare(ASquare):
    """Represents a square on chessboard that contains a piece"""
    def __init__(self, x, y, piece) -> None:
        super().__init__(x, y)
        self.piece = piece

    def empty(self) -> bool:
        return False

    def enemy(self, color: Color) -> bool:
        return self.piece.color != color

    def off_board(self) -> bool:
        return False

    def __repr__(self) -> str:
        return f'[{self.x},{self.y}] {str(self.piece)}'
