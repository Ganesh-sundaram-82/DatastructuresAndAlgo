# # Implement a linked list class. You have to define a few functions that perform the desirbale action. Your `LinkedList` class should be able to:

# # + Append data to the tail of the list and prepend to the head
# # + Search the linked list for a value and return the node
# # + Remove a node
# # + Pop, which means to return the first node's value and delete the node from the list
# # + Insert data at some position in the list
# # + Return the size (length) of the linked list

class node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        # TODO: Write function to prepend here
        prepend= node(value)
        prepend.next= self.head
        self.head = prepend
        # This is the way to add a function to a class after it has been defined
        
    def append(self, value):
        """ Append a value to the end of the list. """    
        # TODO: Write function to append here    
        self.nextNode = node(value)
        if self.head is None:
            self.head = self.nextNode
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = self.nextNode
    pass

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        # TODO: Write function to search here
        tail = self.head
        while tail:
            if tail.value == value:
                return tail
            tail = tail.next
        return None
    pass

# Test prepend
# linked_list = LinkedList()
# linked_list.prepend(1)
# print(linked_list.to_list())
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

# linked_list = LinkedList()
# linked_list.append(1)
# #assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
# print(linked_list.to_list())
# linked_list.append(3)
# #assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"
# print(linked_list.to_list())

# Test search
# linked_list = LinkedList()
# linked_list.prepend(2)
# linked_list.prepend(1)
# linked_list.append(4)
# linked_list.append(3)
# #assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
# #assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"
# print(linked_list.search(1).value)
# print(linked_list.search(4).value)