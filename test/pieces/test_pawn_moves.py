from src.board.board_factory import BoardFactory


def test_white_pawn_moves_len_is_2():
    board = BoardFactory.create()
    moves = board.at(6, 4).piece.available_moves_from(board, 6, 4)
    assert len(moves) == 2


def test_black_pawn_moves_len_is_2():
    board = BoardFactory.create()
    moves = board.piece_at(1, 5).available_moves_from(board, 1, 5)
    assert len(moves) == 2


def test_pawn_first_move():
    board = BoardFactory.create()
    moves = board.piece_at(1, 5).available_moves_from(board, 1, 5)

    assert not board.at(1, 5).empty()
    assert board.at(3, 5).empty()
    moves[0].execute()
    assert board.at(1, 5).empty()
    assert not board.at(3, 5).empty()

    moves = board.piece_at(3, 5).available_moves_from(board, 3, 5)
    assert len(moves) == 1

    moves[0].execute()
    assert board.at(3, 5).empty()
    assert not board.at(4, 5).empty()

    moves = board.piece_at(4, 5).available_moves_from(board, 4, 5)
    assert len(moves) == 1
