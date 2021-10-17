import pytest
from game.tic_tac_game import TicTacGame

@pytest.fixture
def game():
    return TicTacGame()
