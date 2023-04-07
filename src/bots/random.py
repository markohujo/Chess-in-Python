import random

from src.board.board import Board
from src.bots.base import ABot
from src.moves.base import AMove


class RandomBot(ABot):
    """Represents a chess bot that chooses its moves randomly"""

    def find_move(self, board: Board) -> AMove:
        moves = board.generate_possible_moves(self.color)
        return moves[random.randint(0, len(moves) - 1)]
