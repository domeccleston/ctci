class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def create_list(nums, head=None, length=0):
    head = Node(nums[0])
    node = head
    for i in range(1, len(nums)):
        new_node = Node(nums[i])
        node.next = new_node
        node = new_node
    return head


def print_list(head, s=''):
    if head is None:
        return print(s)
    s += str(head.data) + " -> "
    print_list(head.next, s)


def sum_list(l1, l2, carry=0):

    if l1 is None and l2 is None:
        return None

    result = Node()
    value = carry
    new_carry = 0

    if l1 is not None:
        value += l1.data

    if l2 is not None:
        value += l2.data

    result.data = value % 10

    # recurse
    if l1 is not None or l2 is not None:
        if value > 10:
            new_carry = 1
        more = sum_list(l1.next, l2.next, new_carry)
        result.next = more
    
    return result

list1 = create_list([7, 1, 6])
list2 = create_list([5, 9, 2]) # -> 617 + 295 = 912 
print_list(list1)
print_list(list2)
summed_list = sum_list(list1, list2)
print_list(summed_list)
