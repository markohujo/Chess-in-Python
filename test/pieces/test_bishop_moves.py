from src.board.board_factory import BoardFactory
from src.moves.regular import RegularMove


def test_bishop_moves_len_is_0():
    board = BoardFactory.create()
    moves = board.piece_at(7, 2).available_moves_from(board, 7, 2)
    assert len(moves) == 0
    moves = board.piece_at(7, 5).available_moves_from(board, 7, 5)
    assert len(moves) == 0


def test_bishop_moves_multiple():
    board = BoardFactory.create()
    pawn_move = RegularMove(board.at(6, 3), board.at(5, 3), board)
    pawn_move.execute()

    moves = board.piece_at(7, 2).available_moves_from(board, 7, 2)
    assert len(moves) == 5

    bishop_move = RegularMove(board.at(7, 2), board.at(6, 3), board)
    bishop_move.execute()

    assert board.empty_at(7, 2)
    assert not board.empty_at(6, 3)

    moves = board.piece_at(6, 3).available_moves_from(board, 6, 3)
    assert len(moves) == 8

    bishop_move = RegularMove(board.at(6, 3), board.at(5, 4), board)
    bishop_move.execute()

    moves = board.piece_at(5, 4).available_moves_from(board,5, 4)
    assert len(moves) == 9
