from data_structures.queue_ import Queue


def breadth_first(tree):
    output = []
    queue = Queue()
    queue.enqueue(tree.root)

    if tree.root is None:
        return []

    while not queue.is_empty():
        current = queue.dequeue()
        output.append(current.value)
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
    return output
