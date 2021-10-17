import pytest
from game.tic_tac_game import TicTacGame


@pytest.fixture
def game():
   game = TicTacGame()
   return game

@pytest.mark.parametrize(
    "board, win",
    [
        (
            {
                1: "X", 2: "X", 3: "X",
                4: None, 5: None, 6: None,
                7: None, 8: None, 9: None,
            },
            True,   
        ),
        (
            {
                1: "X", 2: "X", 3: "O",
                4: None, 5: None, 6: None,
                7: None, 8: None, 9: None,
            },
            False,     
        ),
        (
            {
                1: "X", 2: None, 3: None,
                4: None, 5: "X", 6: None,
                7: None, 8: None, 9: "X",
            },
            True,   
        ),
        (
            {
                1: None, 2: None, 3: "O",
                4: None, 5: None, 6: "O",
                7: None, 8: None, 9: "O",
            },
            True, 
        ),
        (
            {
                1: None, 2: None, 3: "O",
                4: None, 5: "X", 6: "X",
                7: "O", 8: "O", 9: "X",
            },
            False, 
        ),
    ],
)
def test_should_check_winner(game, board, win):
    game.board = board
    assert game.check_winner() == win