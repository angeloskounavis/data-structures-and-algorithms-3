from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.main = Stack()
        self.holder = Stack()

    def enqueue(self, value):
        """
        Adds a node with value = value to the rear of the pseudo queue.
        """
        while self.main.top:
            self.holder.push(self.main.pop())
        self.main.push(value)
        while self.holder.top:
            self.main.push(self.holder.pop())

    def dequeue(self):
        return self.main.pop()


