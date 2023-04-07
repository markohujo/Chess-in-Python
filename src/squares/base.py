from abc import ABC, abstractmethod

from src.utils.enums.color import Color


class ASquare(ABC):
    """Represents a square (box) on chessboard

    There is 8*8=64 squares in total"""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @abstractmethod
    def empty(self) -> bool:
        """Return True if this square does not contain a piece, False otherwise"""

    @abstractmethod
    def enemy(self, color: Color) -> bool:
        """Return True if this square contains a piece in enemy color, False otherwise"""

    @abstractmethod
    def off_board(self) -> bool:
        """Return True if this square is off-board, False otherwise"""

    @abstractmethod
    def __repr__(self) -> str:
        pass
