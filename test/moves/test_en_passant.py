from src.board.board_factory import BoardFactory
from src.moves.regular import RegularMove


def test_white_en_passant():
    board = BoardFactory.create()

    RegularMove(board.at(6, 5), board.at(4, 5), board).execute()
    RegularMove(board.at(1, 0), board.at(2, 0), board).execute()
    RegularMove(board.at(4, 5), board.at(3, 5), board).execute()
    assert len(board.piece_at(3, 5).valid_moves(board, 3, 5)) == 1

    RegularMove(board.at(1, 6), board.at(3, 6), board).execute()
    assert len(board.piece_at(3, 5).valid_moves(board, 3, 5)) == 2

    RegularMove(board.at(1, 4), board.at(3, 4), board).execute()
    # still expecting len to be 2 because en passant is possible only if the enemy pawn advance in the PREVIOUS move
    assert len(board.piece_at(3, 5).valid_moves(board, 3, 5)) == 2


def test_black_en_passant():
    board = BoardFactory.create()

    RegularMove(board.at(1, 5), board.at(3, 5), board).execute()
    RegularMove(board.at(6, 0), board.at(5, 0), board).execute()
    RegularMove(board.at(3, 5), board.at(4, 5), board).execute()
    assert len(board.piece_at(4, 5).valid_moves(board, 4, 5)) == 1

    RegularMove(board.at(6, 6), board.at(4, 6), board).execute()
    assert len(board.piece_at(4, 5).valid_moves(board, 4, 5)) == 2

    RegularMove(board.at(6, 4), board.at(4, 4), board).execute()
    # still expecting len to be 2 because en passant is possible only if the enemy pawn advance in the PREVIOUS move
    assert len(board.piece_at(4, 5).valid_moves(board, 4, 5)) == 2
