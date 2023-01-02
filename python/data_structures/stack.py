from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Implements the stack data structure.
    """

    def __init__(self, top=None):
        # initialization here
        self.top = top

    def push(self, value):
        """
        Adds a new node to the top of the stack.
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Returns the value from node from the top of the stack and removes that node from the stack.
        """
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            popped = self.top.value
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return popped

    def peek(self):
        """
        Returns the value from node from the top of the stack. Does not modify the stack.
        """
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

    def is_empty(self):
        if self.top:
            return False
        else:
            return True
