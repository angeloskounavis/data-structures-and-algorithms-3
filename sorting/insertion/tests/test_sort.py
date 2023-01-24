import pytest
from insertion.insertion_sort import insertion_sort


def test_happy_path():
    actual = insertion_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_handle_negs():
    actual = insertion_sort([8, -4, -3, 23, 42, 16, 15])
    expected = [-4, -3, 8, 15, 16, 23, 42]
    assert actual == expected


def test_one_el():
    actual = insertion_sort([1])
    expected = [1]
    assert actual == expected


def test_empty():
    with pytest.raises(ValueError):
        insertion_sort([])

