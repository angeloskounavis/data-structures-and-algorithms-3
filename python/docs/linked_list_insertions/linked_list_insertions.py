class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'<Node(val={self.val}, next={self.next})>'


class LinkedList:
    def __init__(self):
        self.head = None
        self.collection = None
        self.up_to_date = True

    # I'm using this as the 'to string' method
    def __str__(self):
        if self.collection and self.up_to_date:
            return self.collection
        else:
            node_list = []
            current = self.head
            while current:
                node_list.append('{' + str(current.val) + '}')
                current = current.next
            node_list.append('None')
            self.collection = ' -> '.join(node_list)
            self.up_to_date = True
            return self.collection

    def insert(self, val):
        new_node = Node(val=val)
        new_node.next = self.head
        self.head = new_node
        self.up_to_date = False

    def includes(self, target):
        current = self.head
        while current:
            if current.val == target:
                return True
            current = current.next
        return False

    def append(self, new_value):
        pass

    def insert_before(self, value, new_value):
        pass

    def insert_after(self, value, new_value):
        pass
    
