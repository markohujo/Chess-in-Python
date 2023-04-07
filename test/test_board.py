from src.board.board_factory import BoardFactory
from src.moves.regular import RegularMove
from src.squares.empty import EmptySquare
from src.utils.enums.color import Color


def test_piece_squares_white():
    piece_squares_test(Color.WHITE)


def test_piece_squares_black():
    piece_squares_test(Color.BLACK)


def test_check():
    board = BoardFactory.create()
    assert not board.check(Color.WHITE)
    assert not board.check(Color.BLACK)

    RegularMove(board.at(6, 4), board.at(4, 4), board).execute()
    RegularMove(board.at(1, 3), board.at(3, 3), board).execute()
    RegularMove(board.at(7, 5), board.at(3, 1), board).execute()

    assert board.check(Color.BLACK)
    assert not board.check(Color.WHITE)


def test_checkmate():
    board = BoardFactory.create()

    assert not board.checkmate(Color.WHITE)
    assert not board.checkmate(Color.BLACK)

    RegularMove(board.at(6, 5), board.at(4, 5), board).execute()
    RegularMove(board.at(1, 4), board.at(3, 4), board).execute()
    RegularMove(board.at(6, 6), board.at(4, 6), board).execute()
    RegularMove(board.at(0, 3), board.at(4, 7), board).execute()

    assert board.checkmate(Color.WHITE)
    assert not board.checkmate(Color.BLACK)


def test_generate_possible_moves():
    board = BoardFactory.create()
    assert len(board.generate_possible_moves(Color.WHITE)) == 20
    assert len(board.generate_possible_moves(Color.BLACK)) == 20


def test_calc_value():
    board = BoardFactory.create()
    assert board.calc_value(Color.WHITE) == board.calc_value(Color.BLACK)

    board.set_square(EmptySquare(0, 0))
    assert board.calc_value(Color.WHITE) > board.calc_value(Color.BLACK)


def test_valid_move():
    board = BoardFactory.create()
    RegularMove(board.at(6, 4), board.at(4, 4), board).execute()
    RegularMove(board.at(7, 5), board.at(3, 1), board).execute()

    move = RegularMove(board.at(1, 3), board.at(2, 3), board)
    assert not board.valid_move(move, Color.BLACK)

    move = RegularMove(board.at(1, 2), board.at(2, 2), board)
    assert board.valid_move(move, Color.BLACK)

    move.execute()

    move = RegularMove(board.at(1, 3), board.at(2, 3), board)
    assert board.valid_move(move, Color.BLACK)
    assert board.valid_move(RegularMove(board.at(2, 2), board.at(3, 2), board), Color.BLACK)

    move.execute()

    move = RegularMove(board.at(2, 2), board.at(3, 2), board)
    assert not board.valid_move(move, Color.BLACK)


def piece_squares_test(color: Color):
    board = BoardFactory.create()

    white_piece_squares = board.piece_squares(color)
    assert len(white_piece_squares) == 16

    for piece_square in white_piece_squares:
        assert not piece_square.empty()
        assert piece_square.piece.color == color
