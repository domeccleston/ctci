"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node,
so as to make a loop in the linked list.

EXAMPLE
Input: A -> B -> C -> D -> E -> C -> Dc[the same C as earlier]
Output: C

input: LinkedListNode head
output: LinkedListNode cyclenode
"""

"""

a -> b -> c -> a
1 -> 2 -> 3 -> 4 -> 5 -> 4
1 -> 2 -> 1

"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def print_list(head, s='', count=0):
    count += 1
    if count > 6:
        return print(s)
    if head is None:
        return print(s)
    s += head.data + ' -> '
    print_list(head.next, s, count)

def loop_detection(head: Node) -> Node:
    node_record = set()
    p = head

    while p is not None:
        if p in node_record:
            return p, p.data
        node_record.add(p)
        p = p.next
    
    return False

def loop_detection1(head: Node) -> Node:
    slow = head
    fast = head

    # find collision point
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if (slow == fast):
            break;

    # error check for if no collision
    if fast is None and fast.next is None:
        return None
    
    # find start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast

    

ll1 = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')

ll1.next = nodeB
ll1.next.next = nodeC
ll1.next.next.next = nodeD
ll1.next.next.next.next = nodeE
ll1.next.next.next.next.next = nodeC

print(loop_detection1(ll1))