# Implement a stack using a linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.num_elements +=1
    
    def pop(self):
        if self.is_empty():
            return None
        self.num_elements -= 1
        tempnode= self.head
        self.head = tempnode.next
        return tempnode.value

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0


# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")
    
        