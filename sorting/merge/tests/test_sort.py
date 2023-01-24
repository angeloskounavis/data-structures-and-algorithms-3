from mergesort import mergesort


def test_happy_path():
    arr = [8, 4, 23, 42, 16, 15]
    actual = mergesort(arr)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_few_uniques():
    arr = [5, 12, 7, 5, 5, 7]
    actual = mergesort(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_odd_length():
    arr = [8, 4, 23, 42, 16, 15, 35]
    actual = mergesort(arr)
    expected = [4, 8, 15, 16, 23, 35, 42]
    assert actual == expected


def test_empty_arr():
    arr = []
    actual = mergesort(arr)
    expected = []
    assert actual == expected
