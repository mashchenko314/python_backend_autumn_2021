import pytest
from my_classes.custom_list import CustomList
import functools

@pytest.mark.parametrize(
    "list_1, list_2, result",
    [
        ( [1,2,3], CustomList([4,5,6,7]), CustomList([5,7,9,7]) ),
        ( CustomList([4,5,6,7]), [1,2,3], CustomList([5,7,9,7]) ),
        ( CustomList([4,5,6,7]), CustomList([1,2,3]), CustomList([5,7,9,7]) )
    ],
)
def test_should_add_correctly(list_1, list_2, result):
    equality_check = True
    amount_list = list_1 + list_2
    for x, y in zip(amount_list, result):
        if x != y:
            equality_check = False
    assert equality_check == True
    assert type(amount_list) == CustomList
    

@pytest.mark.parametrize(
    "list_1, list_2, result",
    [
        ( [1,2,3], CustomList([4,5,6,7]), CustomList([-3,-3,-3,-7]) ),
        ( CustomList([4,5,6,7]), [1,2,3], CustomList([3,3,3,7]) ),
        ( CustomList([4,5,6,7]), CustomList([1,2,3]), CustomList([3,3,3,7]) )
    ],
)
def test_should_sub_correctly(list_1, list_2, result):
    equality_check = True
    difference_list = list_1 - list_2
    for x, y in zip(difference_list, result):
        if x != y:
            equality_check = False
    assert equality_check == True
    assert type(difference_list) == CustomList


def test_immutability_of_list():
    list_1 = CustomList([4,5,6,7])
    list_2 = CustomList([1,5,8,7])
    save_list = list_1
    equality_check = True
    amount_list = list_1 + list_2
    for x, y in zip(save_list, list_1):
        if x != y:
            equality_check = False
    assert equality_check == True
    equality_check = True
    difference_list = list_2 - list_1
    for x, y in zip(save_list, list_1):
        if x != y:
            equality_check = False
    assert equality_check == True


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
    