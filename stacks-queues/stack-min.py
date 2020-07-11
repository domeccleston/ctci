"""
Stack Min: How would you design a stack which,
in addition to push and pop, has a function min which returns the minimum element?
Push, pop and min should all operate in 0(1) time. 
"""

# solution using Python list type

# class Stack:
#     def __init__(self, data=[]):
#         self.items = data
#         self.min = data[0] if len(data) > 0 else None
    
#     def push(self, item):
#         if self.min is None or item < self.min:
#             self.min = item
#         return self.items.append(item)

#     def pop(self):
#         return self.items.pop()
    
#     def _min(self):
#         return self.min

#     def __repr__(self):
#         return str(self.items)

# solution using linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node()
        self.min = Node()
    
    def push(self, item):
        try:
            if self.min.data is None or item < self.min.data:
                new_min_head = Node(item)
                new_min_head.next = self.min
                self.min = new_min_head
        except TypeError:
            pass

        new_head = Node(item)
        new_head.next = self.head
        self.head = new_head

    def pop(self):
        try:
            head = self.head
            self.head = self.head.next
            head.next = None
            return head.data
        except AttributeError:
            raise Exception("Cannot pop from empty stack")

    def _min(self):
        return self.min.data

    def __repr__(self):
        p = self.head
        s = ''

        while p is not None:
            s += str(p.data) + " -> "
            p = p.next

        return s
        


stack = Stack()
stack.push(-1)
stack.push(-2)
stack.push(-3)
stack.push(-1)
stack.push(-10)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.push(-1)
stack.push(-2)
stack.push(-3)
stack.push(-1)
stack.push(-10)
print(stack)