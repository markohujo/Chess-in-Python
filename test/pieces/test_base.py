from src.board.board_factory import BoardFactory
from src.moves.regular import RegularMove


def test_valid_moves_same_as_available():
    board = BoardFactory.create()

    moves = board.piece_at(7, 6).valid_moves(board, 7, 6)
    assert len(moves) == 2

    moves = board.piece_at(6, 6).valid_moves(board, 6, 6)
    assert len(moves) == 2


def test_valid_moves_less_than_available():
    board = BoardFactory.create()

    RegularMove(board.at(6, 4), board.at(4, 4), board).execute()
    RegularMove(board.at(0, 6), board.at(2, 5), board).execute()
    RegularMove(board.at(7, 5), board.at(3, 1), board).execute()

    square = board.at(1, 3)

    available = square.piece.available_moves_from(board, square.x, square.y)
    valid = square.piece.valid_moves(board, square.x, square.y)

    assert len(available) != len(valid)
    assert len(available) == 2
    assert len(valid) == 0


def test_valid_move_to():
    board = BoardFactory.create()

    assert board.piece_at(6, 0).valid_move_to(board, 6, 0, 4, 0) is not None
    assert board.piece_at(6, 0).valid_move_to(board, 6, 0, 3, 0) is None

    RegularMove(board.at(6, 4), board.at(4, 4), board).execute()
    RegularMove(board.at(0, 6), board.at(2, 5), board).execute()
    assert board.piece_at(1, 3).valid_move_to(board, 1, 3, 2, 3) is not None
    RegularMove(board.at(7, 5), board.at(3, 1), board).execute()
    assert board.piece_at(1, 3).valid_move_to(board, 1, 3, 2, 3) is None
