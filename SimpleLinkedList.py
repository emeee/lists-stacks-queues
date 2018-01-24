from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def length(self):
        return self.size

    def insert(self, val):
        node = Node(val)
        if self.isEmpty():
            self.first = node
        else:
            current = self.first
            while current.getNextNode():
                current = current.getNextNode()
            current = current.setNextNode(node)
        self.size += 1

    def get(self, pos):
        current = self.first
        i = 0
        if pos > self.size-1: raise 'Out of bounds'
        while i<pos:
            current = current.getNextNode()
            i += 1
        return current.getVal()

    def delete(self, pos):
        current = self.first
        if pos == 0:
            self.first = current.getNextNode()
        else:
            i = 0
            if pos > self.size-1: raise 'Out of bounds'
            while i<pos:
                previous = current
                current = current.getNextNode()
                i += 1
            later = current.getNextNode()
            previous.setNextNode(later)
        self.size -= 1
