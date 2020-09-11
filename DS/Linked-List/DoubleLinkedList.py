import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node.Node(value)
            self.tail = self.head
            return
            
        self.tail.NextNode = Node.Node(value)
        self.tail.NextNode.PreviousNode = self.tail
        self.tail = self.tail.NextNode
        return
