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
    
    def remove_kth_from_last(self, node, k):
        node_map = {}
        count = 0
        current = node
        prev = None
        print(k)

        while current is not None:
            node_map[count] = (current, prev)
            prev = current
            current = current.next
            count += 1
        
        for i, (key, val) in enumerate(node_map.items()):
            print(key, val)

        to_delete = count - k - 1

        node_map[to_delete][1].next = node_map[to_delete][0].next

        return self


ll = LinkedList(1)

ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)
ll.add_to_tail(5)
ll.add_to_tail(6)
print(ll.remove_kth_from_last(ll.head, 3))