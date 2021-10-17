import pytest
from game.custom_exceptions import InputError
from game.tic_tac_game import TicTacGame


@pytest.fixture
def game():
   game = TicTacGame()
   return game

@pytest.mark.parametrize(
    "item, answer",
    [
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        ("1.0", None),
        ("", None),
        (" ", None),
        ("  ", None),
        ("q", None),
        ("qw", None),
        ("qwe", None),
        ("q1", None),
        ("qw1", None),
        ("qwe3", None),
    ],
)
def test_validate_input(game, item, answer):
    assert game.validate_input(item) == answer