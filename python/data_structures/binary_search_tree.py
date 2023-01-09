from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Implements a binary search tree - left node always less than root, right always greater.
    """

    def __init__(self):
        super().__init__()

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        def helper(root):
            if value > root.value:
                if root.right:
                    helper(root.right)
                else:
                    root.right = Node(value)
            else:
                if root.left:
                    helper(root.left)
                else:
                    root.left = Node(value)

        helper(self.root)

    def contains(self, value):

        def helper(root):
            if not root:
                return False
            if value == root.value:
                return True
            elif value > root.value:
                return helper(root.right)
            elif value < root.value:
                return helper(root.left)

        return helper(self.root)


