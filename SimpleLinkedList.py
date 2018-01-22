class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.nextNode = nextNode

    def setVal(self, val):
        self.val = val

    def getVal(self):
        return self.val

    def setNextNode(self, nextNode):
        self.nextNode = nextNode

    def getNextNode(self):
        return self.nextNode

class SinglyLinkedList:
    def __init__(self):
        self.first = first
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
            aux = self.first
            while aux.getNextNode():
                aux = aux.getNextNode()
            aux = aux.setNextNode(node)
        self.aux = self.aux + 1

    def get(self, pos):
        aux = self.first
        i = 0
        while i<=pos and aux.getNextNode():
            aux = aux.getNextNode()
            i = i + 1
        return aux.getVal()

    def delete(self, pos):
        #TODO
