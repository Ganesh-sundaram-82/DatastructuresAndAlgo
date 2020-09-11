class Stack:
    def __init__(self):
        self.arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.next_index = 0
        self.num_elements = 0

    def push(self, value):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()
        
        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1

    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range( 2* len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

# foo = Stack()
# foo.push("Test") # We first have to push an item so that we'll have something to pop
# print(foo.pop()) # Should return the popped item, which is "Test"
# print(foo.pop())
