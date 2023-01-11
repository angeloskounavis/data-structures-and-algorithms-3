from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(tree):
    """
    returns a "shallow" copy of the current tree as a new tree with the fizzbuzz algorithm applied to each original node's value.
    """
    if not tree.root:
        return KaryTree()

    def fizz_buzz(value):
        if type(value) != int or value < 0:
            return 'not a positive integer'
        elif value % 15 == 0:
            return 'FizzBuzz'
        elif value % 3 == 0:
            return 'Fizz'
        elif value % 5 == 0:
            return 'Buzz'
        else:
            return str(value)

    def walk(source_root, clone_root):
        """
        recursive method to clone Nodes
        """
        if not source_root:
            return

        for source_child in source_root.children:
            clone_child = Node(fizz_buzz(source_child.value))
            clone_root.children.append(clone_child)
            walk(source_child, clone_child)

    clone_tree = KaryTree()

    clone_tree.root = Node(fizz_buzz(tree.root.value))
    walk(tree.root, clone_tree.root)

    return clone_tree
