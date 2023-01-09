from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Implements the queue data structure.
    """

    def __init__(self, front=None):
        self.front = front
        self.rear = front

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.rear = new_node

    def dequeue(self):

        if self.front is None:
            raise InvalidOperationError
        else:
            dequeued = self.front.value
            self.front = self.front.next
            return dequeued

    def peek(self):

        if self.front is None:
            raise InvalidOperationError
        else:
            return self.front.value

    def is_empty(self):
        if self.front:
            return False
        else:
            return True
