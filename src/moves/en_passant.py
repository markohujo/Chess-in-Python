from src.board.board import Board
from src.moves.base import AMove
from src.squares.empty import EmptySquare
from src.squares.piece import PieceSquare


class EnPassant(AMove):
    """Represents en passant move"""

    def __init__(self, square_from: PieceSquare, square_to: EmptySquare, enemy_pawn_square: PieceSquare, board: Board):
        super().__init__(square_from, square_to, board)
        self.enemy_pawn_square = enemy_pawn_square

    def execute(self):
        super().execute()
        self.board.set_square(PieceSquare(self.square_to.x, self.square_to.y, self.square_from.piece))
        self.board.set_square(EmptySquare(self.square_from.x, self.square_from.y))
        self.board.set_square(EmptySquare(self.enemy_pawn_square.x, self.enemy_pawn_square.y))

    def undo(self):
        super().undo()
        self.board.set_square(self.square_from)
        self.board.set_square(self.square_to)
        self.board.set_square(self.enemy_pawn_square)

    def castling(self):
        return False
