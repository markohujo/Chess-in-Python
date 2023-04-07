from src.board.board import Board
from src.board.board_factory import BoardFactory
from src.utils.enums.color import Color
from src.moves.regular import RegularMove


def test_regular_move():
    board = BoardFactory.create()
    move = RegularMove(board.at(6, 5), board.at(4, 5), board)

    assert_before_move(board)

    move.execute()
    assert board.at(6, 5).empty()
    assert not board.at(4, 5).empty()
    assert board.at(4, 5).enemy(Color.BLACK)
    assert not board.at(4, 5).piece.first_move

    move.undo()
    assert_before_move(board)


def test_multiple_regular_moves():
    board = BoardFactory.create()

    move = RegularMove(board.at(6, 5), board.at(4, 5), board)
    move.execute()

    move = RegularMove(board.at(4, 5), board.at(3, 5), board)
    move.execute()
    assert board.at(4, 5).empty()
    assert not board.at(3, 5).empty()

    move.undo()
    assert not board.at(4, 5).empty()
    assert board.at(3, 5).empty()
    assert not board.at(4, 5).piece.first_move


def test_capture_moves():
    board = BoardFactory.create()
    move = RegularMove(board.at(6, 5), board.at(4, 5), board)
    move.execute()
    move = RegularMove(board.at(1, 4), board.at(3, 4), board)
    move.execute()

    assert not board.empty_at(4, 5)
    assert board.enemy_at(4, 5, Color.BLACK)
    assert not board.empty_at(3, 4)
    assert board.enemy_at(3, 4, Color.WHITE)

    capture_move = RegularMove(board.at(4, 5), board.at(3, 4), board)
    capture_move.execute()

    assert board.empty_at(4, 5)
    assert not board.empty_at(3, 4)
    assert board.enemy_at(3, 4, Color.BLACK)


def assert_before_move(board: Board):
    assert not board.at(6, 5).empty()
    assert board.at(4, 5).empty()
    assert not board.at(4, 5).enemy(Color.BLACK)
    assert not board.at(4, 5).enemy(Color.WHITE)
    assert board.at(6, 5).piece.first_move
