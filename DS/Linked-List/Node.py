class Node:
    def __init__(self, data):
        self.value  = data
        self.next = None

testdata = [1, 2, 3, 4, 5, 6]
head = None

for d in testdata:
    tempdata = Node(d)
    if head is None:
        head = tempdata
    else:
        head.next  = tempdata

for value in testdata:
    if head.value != value:
        print(head.value)
    else:
        head = head.next
