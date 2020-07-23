""" 
- init new ll
- iterate through ll1 and ll2 til both of them are not none
- check if a node is none
-   if so, consume the rest of the other list and break
- if node1 is smaller append then node2, else node2 then node1
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def add_to_tail(self, head, value):
        new_tail = ListNode(value)
        p = head
        while p.next is not None:
            p = p.next
        p.next = new_tail

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newLL = ListNode()
        p1 = l1
        p2 = l2
        while p1 is not None or p2 is not None:
            if p1 is None:
                while p2 is not None:
                    self.add_to_tail(newLL, p2.val)
                    p2 = p2.next
                break
            elif p2 is None:
                while p1 is not None:
                    self.add_to_tail(newLL, p1.val)
                    p1 = p1.next
                break
            if p1.val < p2.val:
                self.add_to_tail(newLL, p1.val)
                self.add_to_tail(newLL, p2.val)
            elif p2.val >= p1.val:
                self.add_to_tail(newLL, p2.val)
                self.add_to_tail(newLL, p1.val)      

        p3 = newLL
        while p3 is not None:
            print(p3)
            p3 = p3.next          

                
            

ll1 = ListNode(1)
ll1.next = ListNode(2)
ll1.next.next = ListNode(4)

ll2 = ListNode(1)
ll2.next = ListNode(3)
ll2.next.next = ListNode(4)
ll2.next.next.next = ListNode(5)

s = Solution()
s.mergeTwoLists(ll1, ll2)