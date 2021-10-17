import pytest
from game.custom_exceptions import InputError

@pytest.mark.parametrize(
    "valid_input, return_value",
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
    ],
)
def test_should_return_valid_values(game, valid_input, return_value):
    assert game.validate_input(valid_input) == return_value


@pytest.mark.parametrize(
    "invalid_input",
    ["1.0", "one", "   ", " ", "10", 11, "qwerty1"],
)
def test_should_cause_an_error(game, invalid_input):
    with pytest.raises(InputError) as exc:
        game.validate_input(invalid_input)
    assert exc.type == InputError
