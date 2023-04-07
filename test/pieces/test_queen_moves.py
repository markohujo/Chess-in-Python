from src.board.board_factory import BoardFactory
from src.moves.regular import RegularMove


def test_white_queen_moves():
    board = BoardFactory.create()
    moves = board.piece_at(7, 3).available_moves_from(board, 7, 3)
    assert len(moves) == 0

    pawn_move = RegularMove(board.at(6, 3), board.at(4, 3), board)
    pawn_move.execute()
    moves = board.piece_at(7, 3).available_moves_from(board, 7, 3)
    assert len(moves) == 2

    pawn_move = RegularMove(board.at(6, 4), board.at(4, 4), board)
    pawn_move.execute()
    moves = board.piece_at(7, 3).available_moves_from(board, 7, 3)
    assert len(moves) == 6


def test_black_queen_moves():
    board = BoardFactory.create()
    moves = board.piece_at(0, 3).available_moves_from(board, 0, 3)
    assert len(moves) == 0

    pawn_move = RegularMove(board.at(1, 3), board.at(3, 3), board)
    pawn_move.execute()
    moves = board.piece_at(0, 3).available_moves_from(board, 0, 3)
    assert len(moves) == 2
