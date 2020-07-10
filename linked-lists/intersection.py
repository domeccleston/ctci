"""
Given two (singly) linked lists, determine if the two lists intersect.
Return the inter­secting node. Note that the intersection is defined based on reference,
not value. That is, if the kth node of the first linked list is the exact same node (by reference)
as the jth node of the second linked list, then they are intersecting.

Input: ll1: Node, ll2: Node
Output: intersect: Node
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def create_list(data):
    head = Node(data[0])
    cur = head
    for i in range(1, len(data)):
        cur.next = Node(data[i])
        cur = cur.next
    return head

def print_list(head, s=''):
    if head is None:
        return print(s)
    s += str(head.data) + ' -> '
    print_list(head.next, s)

def intersection(ll1: Node, ll2: Node) -> Node:
    set1 = set()
    set2 = set()
    set3 = set()
    p1 = ll1
    p2 = ll2

    # while p1 is not None or p2 is not None:
    #     if p1 is not None:
    #         set1.add(p1)
    #         p1 = p1.next
    #     if p2 is not None:
    #         set2.add(p2)
    #         p2 = p2.next

    while p1 is not None or p2 is not None:
        if p1 is not None:
            if p1 in set3:
                return True
            set3.add(p1)
            p1 = p1.next
        if p2 is not None:
            if p2 in set3:
                return True
            set3.add(p2)
            p2 = p2.next

    return False

    intersect = set1.intersection(set2)
    if len(intersect) > 0:
        return True
    return False

def intersection2(ll1: Node, ll2: Node) -> Node:
    """Solution using pointers only, accounting for diff lengths"""
    longest = None
    shortest = None
    difference = None

    def find_length_and_tail(head):
        length = 1
        p = head
        while p is not None:
            p = p.next
            length += 1
        
        return length, p
    
    ll1_data = find_length_and_tail(ll1)
    ll2_data = find_length_and_tail(ll2)

    if ll1_data[1] != ll2_data[1]:
        return False
    
    if ll1_data[0] > ll2_data[0]:
        longest = ll1
        shortest = ll2
        difference = ll1_data[0] - ll2_data[0]
    else:
        longest = ll2
        shortest = ll1
        difference = ll2_data[0] - ll1_data[0]

    p_l = longest
    p_s = shortest

    while p_l is not None or p_s is not None:
        while difference > 0:
            p_l = p_l.next
            difference -= 1
        if p_l.data == p_s.data:
            return p_l, p_l.data
        p_l = p_l.next
        p_s = p_s.next

    


ll1 = Node(1)
node2 = Node(2)
node3 = Node(3)
ll2 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

ll1.next = node2
ll1.next.next = node3
ll1.next.next.next = node6 # 1 -> 2 -> 3 -> 6

ll2.next = node5
ll2.next.next = node7
ll2.next.next.next = node3 # 4 -> 5 -> 7 -> 3 -> 6

print(intersection2(ll1, ll2))