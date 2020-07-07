"""
Partition: 

Write code to partition a linked list around a value x,
such that all nodes less than x come before all nodes greater than or equal to x.
If x is contained within the list, the values of x only need to be after the elements less than x 
(see below). The partition element x can appear anywhere in the "right partition"; 
it does not need to appear between the left and right partitions.

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

# 3 -> 2 -> 1->
# 5 -> 8 -> 5 -> 10 ->

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

    def partition(self, value):
        # lower = linkedlist
        # upper = linkedlist
        # iterate through list
        # if item is lower than pivot, add to lower
        # if item is equal to or greater than pivor, add to higher
        # connect tail of lower to head of higher
        # set head of list