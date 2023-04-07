from src.utils.enums.color import Color
from src.squares.base import ASquare


class EmptySquare(ASquare):
    """Represents an empty (does not contain a piece) square on chess board"""

    def empty(self) -> bool:
        return True

    def enemy(self, color: Color) -> bool:
        return False

    def off_board(self) -> bool:
        return False

    def __repr__(self) -> str:
        return f'[{self.x},{self.y}] --'
