import Node

# # head = Node.Node("1")
# # head.NextNode = Node.Node("2")
# # print(head.value)
# # print(head.NextNode.value)

#Single Linked-list

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node.Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.NextNode:
            node = node.NextNode
        
        node.NextNode = Node.Node(value)
        return
    
    def print(self):
        node = self.head
        while node:
            print(node.value)
            node = node.NextNode
    
    def to_list(self):
        self.list = []
        node = self.head
        while node:
            self.list.append(node.value)
            node = node.NextNode
        return self.list
        
        

#Single linked-list Operation
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)
#linked_list.print()
print(linked_list.to_list())
