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

    def remove_duplicates(self, n):
        prev = None;
        duplicates = set()

        while n is not None:
            if n.data in duplicates:
                prev.next = n.next
            else:
                duplicates.add(n.data)
                prev = n
            n = n.next

        return self

    # solution with pointers only

    def remove_duplicates2(self, n):
        current = n

        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

        return self


            



ll = LinkedList(1)

ll.add_to_tail(2)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(1)
ll.add_to_tail(4)
ll.add_to_tail(2)
ll.add_to_tail(5)
ll.add_to_tail(3)
# 1 -> 2 -> 2 -> 3 -> 2 -> 4 -> 2 -> 5 -> 3
print(ll.remove_duplicates(ll.head))
print(ll.remove_duplicates2(ll.head))