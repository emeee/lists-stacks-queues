from node import Node

class Stack:

    def __init__(self):
        self.size = 0
        self.first = None

    def isEmpty(self):
        return self.size == 0

    def push(self, val):
        node = Node(val)
        node.setNextNode(self.first)
        self.first = node
        self.size += 1

    def pop(self):
        old_first = self.first
        self.first = self.first.getNextNode()
        self.size -= 1
        return old_first.getVal()
