class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def print_list(node, s=''):
    if node is None:
        return print(s)
    s += str(node.data) + " -> "
    print_list(node.next, s)

def create_list(word: str) -> Node:
    data = list(word)
    head = Node(data[0])
    p = head

    for i in range(1, len(data)):
        p.next = Node(data[i])
        p = p.next

    return head

def reverse(node: Node) -> Node:
    head = None
    while node is not None:
        n = Node(node.data)
        n.next = head
        head = n
        node = node.next
    return head

list1 = create_list("hello")
revlist = reverse(list1)
print_list(list1)
print_list(revlist)