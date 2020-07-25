""" 
- init new ll
- iterate through ll1 and ll2 til both of them are not none
- check if a node is none
-   if so, consume the rest of the other list and break
- if node1 is smaller append then node2, else node2 then node1

1 -> 3 -> 4-> 
1 -> 2 -> 4 ->

1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newLL = ListNode()
        p1 = l1
        p2 = l2
        p3 = newLL
        final = newLL

        while p1 is not None or p2 is not None:

            if p1 is None:
                while p2 is not None:
                    p3.next = ListNode(p2.val)
                    p3 = p3.next
                    p2 = p2.next
            elif p2 is None:
                while p1 is not None:
                    p3.next = ListNode(p1.val)
                    p3 = p3.next
                    p1 = p1.next   

            elif p1 is not None and p2 is not None:             
                if p1.val < p2.val:
                    p3.next = ListNode(p1.val)
                    p1 = p1.next
                    p3 = p3.next
                elif p2.val <= p1.val:
                    p3.next = ListNode(p2.val)
                    p2 = p2.next
                    p3 = p3.next

        final = final.next

        while final is not None:
            print(final.val)
            final = final.next
            

ll1 = ListNode(1)
ll1.next = ListNode(2)

ll2 = ListNode(10)
ll2.next = ListNode(20)


s = Solution()
s.mergeTwoLists(ll1, ll2)