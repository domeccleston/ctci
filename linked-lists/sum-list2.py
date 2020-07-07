# LeetCode version
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        new_list = ListNode()
        carry = 0
        remainder = None
        
        while p1 is not None and p2 is not None:
            val1 = p1.val
            val2 = p2.val
            _sum = val1 + val2 + carry
            if len(str(_sum)) == 2:
                carry = 1
            else:
                carry = 0
            new_value = int(str(_sum)[-1:])
            new_list.next = ListNode(new_value)
            p1 = p1.next
            p2 = p2.next
        
        return new_list
            
        
