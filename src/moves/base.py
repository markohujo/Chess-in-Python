from abc import ABC, abstractmethod

from src.board.board import Board


class AMove(ABC):

    def __init__(self, square_from, square_to, board: Board) -> None:
        self.square_from = square_from
        self.square_to = square_to
        self.board = board
        self.last_move_tmp = self.board.last_move

    @abstractmethod
    def execute(self) -> None:
        self.board.last_move = self

    @abstractmethod
    def undo(self) -> None:
        self.board.last_move = self.last_move_tmp

    @abstractmethod
    def castling(self):
        pass

    def match(self, src_x: int, src_y: int, dest_x: int, dest_y: int) -> bool:
        return self.square_from.x == src_x and self.square_from.y == src_y and \
               self.square_to.x == dest_x and self.square_to.y == dest_y

    def __str__(self) -> str:
        return f'[{self.square_from.x},{self.square_from.y}] -> [{self.square_to.x},{self.square_to.y}]'
