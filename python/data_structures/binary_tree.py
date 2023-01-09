import math


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class BinaryTree:
    """
    Holds all the attributes and methods necessary to implement a binary tree.
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        tree_arr = []

        def helper(root):
            tree_arr.append(root.value)
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)

        helper(self.root)
        return tree_arr

    def in_order(self):
        tree_arr = []

        def helper(root):
            if root.left:
                helper(root.left)
            tree_arr.append(root.value)
            if root.right:
                helper(root.right)

        helper(self.root)
        return tree_arr

    def post_order(self):
        tree_arr = []

        def helper(root):

            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
            tree_arr.append(root.value)

        helper(self.root)
        return tree_arr

    def find_maximum_value(self):
        tree_max = float('-inf')

        if not self.root:
            return None

        def helper(root):
            nonlocal tree_max
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)

            if root.value > tree_max:
                tree_max = root.value

        helper(self.root)
        return tree_max

