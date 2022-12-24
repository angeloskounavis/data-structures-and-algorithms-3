import pytest
from linked_list import Node, LinkedList

# Can successfully instantiate an empty linked list
# Can properly insert into the linked list
# The head property will properly point to the first node in the linked list
# Can properly insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists
# Will return false when searching for a value in the linked list that does not exist
# Can properly return a collection of all the values that exist in the linked list


def test_node_proof_of_life():
    assert Node


def test_ll_proof_of_life():
    assert LinkedList


def test_can_instantiate_ll():
    actual = LinkedList()
    assert type(actual) == LinkedList


def test_insert():
    new_ll = LinkedList()
    new_ll.insert(4)
    actual = new_ll
    expected = '{4} -> None'
    assert actual.__str__() == expected


def test_head_points_to_first_node():
    new_ll = LinkedList()
    new_ll.insert(4)
    actual = new_ll.head
    expected = Node(4)
    assert actual.__repr__() == expected.__repr__()


def test_multiple_insertions():
    new_ll = LinkedList()
    new_ll.insert(4)
    new_ll.insert(5)
    actual = new_ll
    expected = '{5} -> {4} -> None'
    assert actual.__str__() == expected


def test_does_include_val():
    new_ll = LinkedList()
    new_ll.insert(4)
    actual = new_ll.includes(4)
    expected = True
    assert actual == expected


def test_does_not_include_val():
    new_ll = LinkedList()
    new_ll.insert(4)
    actual = new_ll.includes(5)
    expected = False
    assert actual == expected


def test_print_collection_of_values():
    new_ll = LinkedList()
    new_ll.insert(4)
    new_ll.insert(5)
    new_ll.insert(6)
    actual = new_ll
    expected = '{6} -> {5} -> {4} -> None'
    assert actual.__str__() == expected
