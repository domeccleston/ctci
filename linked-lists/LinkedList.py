class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
        self.length = 1 if value is not None else 0
    
    def __repr__(self):
        p = self.head
        s = ''
        while p is not None:
            s += str(p.data) + " -> "
            p = p.next
        return s

    def add_to_tail(self, value):
        new_tail = Node(value)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = new_tail
        self.length += 1