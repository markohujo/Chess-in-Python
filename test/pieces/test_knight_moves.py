from src.board.board_factory import BoardFactory
from src.moves.regular import RegularMove


def test_knight_moves_len_is_2():
    board = BoardFactory.create()
    moves = board.piece_at(7, 1).available_moves_from(board, 7, 1)
    assert len(moves) == 2
    moves = board.piece_at(7, 6).available_moves_from(board, 7, 6)
    assert len(moves) == 2


def test_knight_moves_len_is_5():
    board = BoardFactory.create()
    move = RegularMove(board.at(7, 1), board.at(5, 2), board)
    move.execute()

    moves = board.piece_at(5, 2).available_moves_from(board, 5, 2)
    assert len(moves) == 5
