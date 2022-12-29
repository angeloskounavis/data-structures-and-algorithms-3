class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'<Node(val={self.value}, next={self.next})>'


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.collection = None
        self.up_to_date = True

    def __str__(self):
        if self.collection and self.up_to_date:
            return self.collection
        else:
            node_list = []
            current = self.head
            while current:
                node_list.append('{ ' + str(current.value) + ' }')
                current = current.next
            node_list.append('NULL')
            self.collection = ' -> '.join(node_list)
            self.up_to_date = True
            return self.collection

    def insert(self, val):
        new_node = Node(value=val)
        new_node.next = self.head
        self.head = new_node
        self.up_to_date = False

    def includes(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def append(self, new_value):
        new_node = Node(new_value)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, target, new_value):
        new_node = Node(new_value)
        print(new_node)
        current = self.head

        if self.head is None:
            raise TargetError("Empty list.")

        if current.value == target:
            new_node.next = current
            self.head = new_node
        else:
            while current.next:
                if current.next.value == target:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next

            raise TargetError('Target not found.')

    def insert_after(self, target, new_value):
        new_node = Node(new_value)
        current = self.head

        if self.head is None:
            raise TargetError("Empty list.")

        while current.next:
            if current.value == target:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                current = current.next

        raise TargetError('Target not found.')

    def kth_from_end(self, k):
        '''
        Returns the value of the kth node from the tail of the linked list.
        '''
        new_list = []
        current = self.head

        if k < 0:
            raise TargetError('k is under range. Input an integer >= 0')

        while current:
            new_list.append(current.value)
            current = current.next

        if abs(-1 - k) > len(new_list):
            raise TargetError('k is out of range')
        else:
            return new_list[-1 - k]


class TargetError(Exception):
    def __init__(self, message):
        self.message = message
