import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_get_apple(): # tests get and set
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    print(hashtable.hash('ahmad'), hashtable.hash('silent'), hashtable.hash('listen'))

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    actual = sorted(actual, key= lambda x: x[0], reverse= True)
    expected = [[["silent", True]], [["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected


def test_get_null():# tests returning null for a value not in table
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("orange")
    expected = None
    assert actual == expected


def test_keys_method():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    expected = ['ahmad', 'listen', 'silent']
    actual = hashtable.keys()
    assert actual == expected


def test_collision():
    hashtable = Hashtable(1)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    print(hashtable)

    actual = hashtable.get('silent')
    expected = True

    assert actual == expected


def test_hash_in_range():
    hashtable = Hashtable(1024)
    actual = hashtable.hash('So long and thanks for all the fish')
    assert actual in range(1024)

