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
