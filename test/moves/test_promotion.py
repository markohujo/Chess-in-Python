from src.board.board_factory import BoardFactory
from src.moves.en_passant import EnPassant
from src.moves.promotion import Promotion
from src.moves.regular import RegularMove
from src.utils.enums.color import Color
from src.utils.enums.piece_type import PieceType


def test_promotion():
    board = BoardFactory.create()

    RegularMove(board.at(6, 0), board.at(4, 0), board).execute()
    RegularMove(board.at(4, 0), board.at(3, 0), board).execute()
    RegularMove(board.at(1, 1), board.at(3, 1), board).execute()
    EnPassant(board.at(3, 0), board.at(2, 1), board.at(3, 1), board).execute()
    RegularMove(board.at(2, 1), board.at(1, 1), board).execute()

    moves = board.piece_at(1, 1).valid_moves(board,1, 1)
    assert len(moves) == 2

    Promotion(board.at(1, 1), board.at(0, 0), board).execute()
    assert board.piece_at(0, 0).color == Color.WHITE
    assert board.piece_at(0, 0).type() == PieceType.QUEEN
