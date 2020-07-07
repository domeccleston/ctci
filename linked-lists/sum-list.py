"""
Sum Lists: You have two numbers represented by a linked list,
where each node contains a single digit. The digits are stored in reverse order,
such that the 1 's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE

Input: (7-> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295. Output: 2 -> 1 -> 9. That is, 912.

617 + 
295 = 912
        2 | 1
       1  | 1
      9

2467
34152 = 36619

    9
   1  | 1
  6    
 6
3 

2467
3815 = 6282 | 1
            



987 +
765 = 1752
         2  | 1
        5   | 1
       7    | 1
      1 

7+5 = 12 -> 2 | 1
8+6 = 14 = > 3 | 1
7+9 = 16 -> 6 | 1



FOLLOW UP

Suppose the digits are stored in forward order. Repeat the above problem. 

EXAMPLE

Input:(6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295. Output: 9 -> 1 -> 2. That is, 912.
"""

import unittest

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

def sum_list(listA, listB):
    pA = listA.head
    pB = listB.head
    new_list = LinkedList()
    carry = 0
    remainder = None

    while pA is not None and pA is not None:
        valA = pA.data
        valB = pB.data
        _sum = valA + valB + carry
        if len(str(_sum)) == 2:
            carry = 1
        else:
            carry = 0
        new_value = int(str(_sum)[-1:])
        new_list.add_to_tail(new_value)
        pA = pA.next
        pB = pB.next

    if pA is not None:
        while pA is not None:
            valA = pA.data
            _sum = valA + carry
            if len(str(_sum)) == 2:
                carry = 1
            else:
                carry = 0
            new_value = int(str(_sum)[-1:])
            new_list.add_to_tail(new_value)
            pA = pA.next

    elif pB is not None:
        while pB is not None:
            valB = pB.data
            _sum = valB + carry
            if len(str(_sum)) == 2:
                carry = 1
            else:
                carry = 0
            new_value = int(str(_sum)[-1:])
            new_list.add_to_tail(new_value)
            pB = pB.next

    new_list.head = new_list.head.next

    return new_list


def create_list(nums):
    head = LinkedList(nums[0])
    for i in range(1, len(nums)):
        head.add_to_tail(nums[i])
    return head


sum1 = create_list([7, 6, 4, 2])
sum2 = create_list([2, 5, 1, 4, 3])
print(sum_list(sum1, sum2))

# sum3 = create_list([3, 4, 2, 0, 0, 2, 1, 4])
# sum4 = create_list([4, 8, 9, 6, 3, 2, 1, 0])

# class TestSumList(unittest.TestCase):

#     def test_basic(self):
#         self.assertEqual(sum_list(sum1, sum2), '9 -> 1 -> 6 -> 6 -> 3 ->')


# if __name__ == "__main__":
#     unittest.main()
