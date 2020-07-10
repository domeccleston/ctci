"""Palindrome: Implement a function to check if a linked list is a palindrome.

NOTES

- takes linked list as input, so we need at least a Node class
- assume this returns True if list is palindrome, else False
- What is a palindrome? In this context, a linked list that is equal to itself, reversed
- if reverse(ll) == ll: True
"""

import math

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


def palindrome(head: Node) -> Node:
    p = head
    index = 0
    node_dict = dict()

    if head.data is None:
        raise ValueError("Node data must not be null")

    while p is not None:
        node_dict[index] = p.data # lower(str(p.data)) if we want to ignore uppercase
        index += 1
        p = p.next

    length = len(node_dict.keys())
    midpoint_index = math.ceil(length / 2) - 1
    count = 0

    for i in range(length - 1, midpoint_index, -1):
        if node_dict[count] != node_dict[i]:
            return False
        count += 1

    return True

# O(n) solution using a stack and two pointer approach - not fully implemented
def palindrome1(head: Node) -> Node:
    slow = head
    fast = head
    stack = []

    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next


    if fast is not None:
        slow = slow.next

    while slow is not None:
        top = stack.pop()

        if top != slow.data:
            return False
        
        slow = slow.next
    
    return True

def palindrome2()



# ll = Node("m")
# ll.next = Node("a")
# ll.next.next = Node("p")
# ll.next.next.next = Node("a")
# ll.next.next.next.next = Node("m")
# print_list(ll)
# print(palindrome(ll))

ll = create_list("apamapa") # expect True
ll1 = create_list("bob") # expect True
ll2 = create_list("panama") # expect False
ll3 = create_list("Heheh") # expect False
ll4 = create_list("123321") # expect True


badll = Node(None)
badll.next = Node(None)
badll.next.next = Node(None)

print(palindrome1(ll))
print(palindrome1(ll1))
print(palindrome1(ll2))
print(palindrome1(ll3))
print(palindrome1(ll4))
# print(palindrome(badll))