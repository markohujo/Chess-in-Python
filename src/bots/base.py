from abc import ABC, abstractmethod

from src.board.board import Board
from src.moves.base import AMove
from src.utils.enums.color import Color


class ABot(ABC):
    """Represents a bot playing chess"""

    def __init__(self, color: Color) -> None:
        self.color = color

    def take_turn(self, board: Board) -> None:
        """Execute exactly one move chosen by the result of find_move of this bot"""
        self.find_move(board).execute()

    @abstractmethod
    def find_move(self, board: Board) -> AMove:
        """Return move that will be executed"""
        pass
