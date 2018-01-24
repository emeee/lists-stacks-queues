from node import Node

class Queue:

    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, val):
        node = Node(val)
        if self.isEmpty():
            self.first = node
        else:
            self.last.setNextNode(node)
        self.last = node
        self.size += 1

    def getFirst(self):
        return self.first

    def dequeue(self):
        old_first = self.first
        self.first = self.first.getNextNode()
        self.size -= 1
        return old_first.getVal()
