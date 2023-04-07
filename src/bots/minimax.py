from src.board.board import Board
from src.bots.base import ABot
from src.moves.base import AMove
from src.utils.color_converter import ColorConverter
from src.utils.enums.color import Color

DEPTH = 3
INT_LIMIT = 2147483647
INT_MIN = -INT_LIMIT
INT_MAX = INT_LIMIT


class MinimaxBot(ABot):
    """Represents a bot that calculates board value in order to choose its best move"""

    def __init__(self, color: Color, depth: int = DEPTH) -> None:
        super().__init__(color)
        self.depth = depth

    def find_move(self, board: Board) -> AMove:
        best_value = INT_MIN
        best_move = None

        for move in board.generate_possible_moves(self.color):

            if move.castling() and board.check(self.color):
                continue

            move.execute()
            value = self.__minimax(board, INT_MIN, INT_MAX, self.depth - 1, False, ColorConverter.convert(self.color))
            move.undo()

            if value > best_value:
                best_value = value
                best_move = move

        return best_move

    def __minimax(self, board: Board, alpha: int, beta: int, depth: int, is_max: bool, color: Color) -> int:
        if depth == 0:
            return board.calc_value(self.color)

        if is_max:
            for move in board.generate_possible_moves(color):

                if move.castling() and board.check(color):
                    continue

                move.execute()
                value = self.__minimax(board, alpha, beta, depth - 1, False, ColorConverter.convert(color))
                move.undo()

                if value >= beta:
                    return beta
                alpha = max(alpha, value)

            return alpha

        else:
            for move in board.generate_possible_moves(color):

                if move.castling() and board.check(color):
                    continue

                move.execute()
                value = self.__minimax(board, alpha, beta, depth - 1, True, ColorConverter.convert(color))
                move.undo()

                if value <= alpha:
                    return alpha
                beta = min(beta, value)

            return beta
