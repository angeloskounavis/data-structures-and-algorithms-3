class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'<Node(val={self.val}, next={self.next})>'


class LinkedList:
    def __init__(self):
        self.head = None

    # I'm using this as the 'to string' method
    def __str__(self):
        node_list = []
        current = self.head
        while current:
            node_list.append('{' + str(current.val) + '}')
            current = current.next
        node_list.append('None')
        return ' -> '.join(node_list)

    def insert(self, val):
        new_node = Node(val=val)
        new_node.next = self.head
        self.head = new_node

    def includes(self, target):
        current = self.head
        while current:
            if current.val == target:
                return True
            current = current.next
        return False

