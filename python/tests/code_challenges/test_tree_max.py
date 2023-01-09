import pytest
from data_structures.binary_tree import BinaryTree, Node


def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


def test_deeper_tree_max(numeric_tree):
    actual = numeric_tree.find_maximum_value()
    expected = 9
    assert actual == expected


def test_negative_tree_max(negative_tree):
    actual = negative_tree.find_maximum_value()
    expected = -1
    assert actual == expected


def test_tree_max_empty_tree():
    tree = BinaryTree()
    actual = tree.find_maximum_value()
    expected = None
    assert actual == expected


@pytest.fixture
def numeric_tree():
    """
          1
      4      6
    3  5    8  9
    """

    num_tree = BinaryTree()

    num_tree.root = Node(1)
    num_tree.root.left = Node(4)
    num_tree.root.right = Node(6)
    num_tree.root.left.left = Node(3)
    num_tree.root.left.right = Node(5)
    num_tree.root.right.left = Node(8)
    num_tree.root.right.right = Node(9)

    return num_tree


@pytest.fixture
def negative_tree():
    """
          -5
      -4      -6
    -3  -1    -8  -9
    """

    num_tree = BinaryTree()

    num_tree.root = Node(-5)
    num_tree.root.left = Node(-4)
    num_tree.root.right = Node(-6)
    num_tree.root.left.left = Node(-3)
    num_tree.root.left.right = Node(-1)
    num_tree.root.right.left = Node(-8)
    num_tree.root.right.right = Node(-9)

    return num_tree
