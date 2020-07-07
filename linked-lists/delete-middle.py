class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data)
        self.length = 1 if data is not None else 0

    def __repr__(self):
        p = self.head
        s = ''
        while p is not None:
            s += f'{p.data} -> '
            p = p.next
        return s

    def add_to_tail(self, data):
        new_tail = Node(data)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = new_tail
        self.length += 1

    def delete_node_from_middle(self, node):
        if node is None or node.next is None:
            return False
        next_node = node.next
        node.data = next_node.data
        n.next = next_node.next
        return True

ll = LinkedList(1)
ll.add_to_tail(2)
ll.add_to_tail(3)
ll.add_to_tail(4)
ll.add_to_tail(5)
print(ll)