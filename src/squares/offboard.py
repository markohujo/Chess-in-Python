from src.utils.enums.color import Color
from src.squares.base import ASquare


class OffBoardSquare(ASquare):
    """Represents a square that is out of bounds"""
    def __init__(self) -> None:
        super().__init__(-1, -1)

    def empty(self) -> bool:
        return False

    def enemy(self, color: Color) -> bool:
        return False

    def off_board(self) -> bool:
        return True

    def __repr__(self) -> str:
        return "OFF BOARD"
