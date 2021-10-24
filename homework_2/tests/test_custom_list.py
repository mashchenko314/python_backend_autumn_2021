import pytest
from my_classes.custom_list import CustomList

@pytest.mark.parametrize(
    "list_1, list_2, result",
    [
        ( [1,2,3], CustomList([4,5,6,7]), CustomList([5,7,9,7]) ),
        ( CustomList([4,5,6,7]), [1,2,3], CustomList([5,7,9,7]) ),
        ( CustomList([4,5,6,7]), CustomList([1,2,3]), CustomList([5,7,9,7]) )
    ],
)
def test_should_add_correctly(list_1, list_2, result):
    assert list_1 + list_2 == result

@pytest.mark.parametrize(
    "list_1, list_2, result",
    [
        ( [1,2,3], CustomList([4,5,6,7]), CustomList([-3,-3,-3,-7]) ),
        ( CustomList([4,5,6,7]), [1,2,3], CustomList([3,3,3,7]) ),
        ( CustomList([4,5,6,7]), CustomList([1,2,3]), CustomList([3,3,3,7]) )
    ],
)
def test_should_sub_correctly(list_1, list_2, result):
    assert list_1 - list_2 == result


@pytest.mark.parametrize(
    "list_1, list_2, result",
    [
        ( CustomList([4,5,6,7]), CustomList([4,5,6,7]), True ),
        ( CustomList([4,5,6,7]), CustomList([4,5,6,9]), False ),
    ],
)
def test_should_eq_correctly(list_1, list_2, result):
    assert (list_1 == list_2) == result

@pytest.mark.parametrize(
    "list_1, list_2, result",
    [
        ( CustomList([4,5,6,7]), CustomList([4,5,6,7]), False ),
        ( CustomList([4,5,6,7]), CustomList([4,5,6,9]), False ),
        ( CustomList([4,5,6,10]), CustomList([4,5,6,7]), True ),
    ],
)
def test_should_gt_correctly(list_1, list_2, result):
    assert (list_1 > list_2) == result

@pytest.mark.parametrize(
    "list_1, list_2, result",
    [
        ( CustomList([4,5,6,7]), CustomList([4,5,6,7]), False ),
        ( CustomList([4,5,6,7]), CustomList([4,5,6,9]), True ),
        ( CustomList([4,5,6,10]), CustomList([4,5,6,7]), False ),
    ],
)
def test_should_lt_correctly(list_1, list_2, result):
    assert (list_1 < list_2) == result
    