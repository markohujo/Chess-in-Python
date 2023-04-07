from src.board.board_factory import BoardFactory
from src.moves.regular import RegularMove


def test_king_moves():
    board = BoardFactory.create()
    moves = board.piece_at(7, 4).available_moves_from(board, 7, 4)
    assert len(moves) == 0

    pawn_move = RegularMove(board.at(6, 3), board.at(4, 3), board)
    pawn_move.execute()
    moves = board.piece_at(7, 4).available_moves_from(board, 7, 4)
    assert len(moves) == 1

    pawn_move = RegularMove(board.at(6, 4), board.at(4, 4), board)
    pawn_move.execute()
    moves = board.piece_at(7, 4).available_moves_from(board, 7, 4)
    assert len(moves) == 2


def test_short_castling():
    board = BoardFactory.create()

    # modify board so castling is possible and valid move
    knight_move = RegularMove(board.at(7, 6), board.at(5, 5), board)
    pawn_move = RegularMove(board.at(6, 6), board.at(5, 6), board)
    bishop_move = RegularMove(board.at(7, 5), board.at(6, 6), board)
    knight_move.execute()
    pawn_move.execute()
    bishop_move.execute()

    moves = board.piece_at(7, 4).available_moves_from(board, 7, 4)
    assert len(moves) == 2
    assert not board.empty_at(7, 4)
    assert board.empty_at(7, 5)
    assert board.empty_at(7, 6)
    assert not board.empty_at(7, 7)
    assert board.piece_at(7, 4).first_move
    assert board.piece_at(7, 7).first_move

    moves[0].execute()
    assert board.empty_at(7, 4)
    assert not board.empty_at(7, 5)
    assert not board.empty_at(7, 6)
    assert board.empty_at(7, 7)
    assert not board.piece_at(7, 5).first_move
    assert not board.piece_at(7, 6).first_move

    moves[0].undo()
    assert not board.empty_at(7, 4)
    assert board.empty_at(7, 5)
    assert board.empty_at(7, 6)
    assert not board.empty_at(7, 7)
    assert board.piece_at(7, 4).first_move
    assert board.piece_at(7, 7).first_move


def test_long_castling():
    board = BoardFactory.create()

    # modify board so castling is possible and valid move
    knight_move = RegularMove(board.at(7, 1), board.at(5, 2), board)
    pawn_move = RegularMove(board.at(6, 3), board.at(4, 3), board)
    queen_move = RegularMove(board.at(7, 3), board.at(5, 3), board)
    bishop_move = RegularMove(board.at(7, 2), board.at(6, 3), board)
    knight_move.execute()
    pawn_move.execute()
    queen_move.execute()
    bishop_move.execute()

    moves = board.piece_at(7, 4).available_moves_from(board, 7, 4)
    assert len(moves) == 2
    assert not board.empty_at(7, 4)
    assert board.empty_at(7, 3)
    assert board.empty_at(7, 2)
    assert board.empty_at(7, 1)
    assert not board.empty_at(7, 0)
    assert board.piece_at(7, 4).first_move
    assert board.piece_at(7, 0).first_move

    moves[0].execute()
    assert board.empty_at(7, 4)
    assert not board.empty_at(7, 3)
    assert not board.empty_at(7, 2)
    assert board.empty_at(7, 1)
    assert board.empty_at(7, 0)
    assert not board.piece_at(7, 2).first_move
    assert not board.piece_at(7, 3).first_move

    moves[0].undo()
    assert not board.empty_at(7, 4)
    assert board.empty_at(7, 3)
    assert board.empty_at(7, 2)
    assert board.empty_at(7, 1)
    assert not board.empty_at(7, 0)
    assert board.piece_at(7, 4).first_move
    assert board.piece_at(7, 0).first_move
