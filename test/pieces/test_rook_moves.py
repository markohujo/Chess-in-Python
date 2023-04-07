from src.board.board_factory import BoardFactory
from src.utils.enums.color import Color
from src.moves.regular import RegularMove


def test_white_rook_moves_len_is_0():
    board = BoardFactory.create()
    moves = board.piece_at(7, 0).available_moves_from(board, 7, 0)
    assert len(moves) == 0
    moves = board.piece_at(7, 7).available_moves_from(board, 7, 7)
    assert len(moves) == 0


def test_black_rook_moves_len_is_0():
    board = BoardFactory.create()
    moves = board.piece_at(0, 0).available_moves_from(board, 0, 0)
    assert len(moves) == 0
    moves = board.piece_at(0, 7).available_moves_from(board, 0, 7)
    assert len(moves) == 0


def test_white_rook_moves_up_once():
    board = BoardFactory.create()
    move_up_once(board)


def test_white_rook_moves_up_multiple():
    board = BoardFactory.create()
    move_up_once(board)

    pawn_move = RegularMove(board.at(4, 0), board.at(3, 0), board)
    pawn_move.execute()
    moves = board.piece_at(7, 0).available_moves_from(board,7, 0)
    assert len(moves) == 3

    pawn_move = RegularMove(board.at(3, 0), board.at(2, 0), board)
    pawn_move.execute()
    moves = board.piece_at(7, 0).available_moves_from(board, 7, 0)
    assert len(moves) == 4

    enemy_capture = RegularMove(board.at(1, 1), board.at(2, 0), board)
    enemy_capture.execute()
    assert board.enemy_at(2, 0, Color.WHITE)

    moves = board.piece_at(7, 0).available_moves_from(board, 7, 0)
    assert len(moves) == 5

    rook_capture = RegularMove(board.at(7, 0), board.at(2, 0), board)
    rook_capture.execute()
    assert not board.empty_at(2, 0)
    assert board.empty_at(7, 0)
    assert not board.enemy_at(2, 0, Color.WHITE)

    moves = board.piece_at(2, 0).available_moves_from(board, 2, 0)
    assert len(moves) == 13


def move_up_once(board):
    pawn_move = RegularMove(board.at(6, 0), board.at(4, 0), board)
    pawn_move.execute()
    moves = board.piece_at(7, 0).available_moves_from(board, 7, 0)
    assert len(moves) == 2
