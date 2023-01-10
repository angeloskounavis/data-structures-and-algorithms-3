import pytest
from data_structures.binary_tree import BinaryTree, Node


def test_exists():
    assert BinaryTree


def test_pre_order(tree):
    actual = tree.pre_order()
    expected = ["a", "b", "d", "e", "c", "f", "g"]
    assert actual == expected


def test_in_order(tree):
    actual = tree.in_order()
    expected = ["d", "b", "e", "a", "f", "c", "g"]
    assert actual == expected


def test_post_order(tree):
    actual = tree.post_order()
    expected = ["d", "e", "b", "f", "g", "c", "a"]
    assert actual == expected


def test_tree_max(numeric_tree):
    actual = numeric_tree.find_maximum_value()
    expected = 9
    assert actual == expected


def test_tree_max_empty_tree():
    tree = BinaryTree()
    actual = tree.find_maximum_value()
    expected = None
    assert actual == expected


@pytest.fixture
def tree():
    """
          a
      b      c
    d  e    f  g
    """

    tree = BinaryTree()

    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")

    return tree


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
