# solution using linked list
# class ListNode:
#     def __init__(self, key=None, value=None, prev=None, next=None):
#         self.key = key
#         self.value = value
#         self.prev = prev
#         self.next = next


# class LinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 0

#     def delete(self, node):
#         if not self.head and not self.tail:
#             return -1

#         else:
#             self.length -= 1

#             if self.head == self.tail:
#                 self.head = None
#                 self.tail = None

#             elif node is self.head:
#                 self.head = self.head.next

#             elif node is self.tail:
#                 self.tail = self.tail.prev

#             if node.next is not None:
#                 node.next.prev = node.prev

#             if node.prev is not None:
#                 node.prev.next = node.next

#     def add_to_tail(self, key, value):
#         new_node = ListNode(key, value)
#         self.length += 1
#         # if list is of length 0, node is both head and tail
#         if not self.head and not self.tail:
#             self.head = new_node
#             self.tail = new_node
#         # otherwise set the new node's prev, and link it with the current tail's next
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node

#         return new_node


# class LRUCache:
#     def __init__(self, capacity: int):
#         self.queue = LinkedList()
#         self.ht = {}
#         self.capacity = capacity

#     def print_cache(self):
#         print("\nht:")
#         for i, (k, v) in enumerate(self.ht.items()):
#             print(f"{k}: ({v.key}, {v.value})")
#         print("\nqueue:")
#         node = self.queue.head
#         while node is not None:
#             print(f"{node.key, node.value} -> ", end="")
#             node = node.next
#         print("\n")

#     def get(self, key: int) -> int:
#         if not key in self.ht:
#             return -1
#         node = self.ht[key]
#         self.queue.delete(node)
#         new_address = self.queue.add_to_tail(key, node.value)
#         self.ht[key] = new_address
#         return node.value

#     def put(self, key: int, value: int) -> None:
#         if key in self.ht:
#             current_node = self.ht[key]
#             self.queue.delete(current_node)
#             new_tail = self.queue.add_to_tail(key, value)
#             self.ht[key] = new_tail
#         else:
#             if self.queue.length < self.capacity:
#                 new_tail = self.queue.add_to_tail(key, value)
#                 self.ht[key] = new_tail
#             else:
#                 head_key = self.queue.head.key
#                 self.queue.delete(self.queue.head)
#                 del self.ht[head_key]
#                 new_tail = self.queue.add_to_tail(key, value)
#                 self.ht[key] = new_tail


# solution using list

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache = {}
        self._usage = []

    @property
    def _isFull(self):
        return len(self._cache.keys()) > self.capacity
    
    def _move_to_end(self, key):
        if key in self._usage:
            self._usage = [k for k in self._usage if k != key]
        self._usage.append(key)

    def get(self, key: int) -> int:
        value = self._cache.get(key, -1)
        if value != -1:
            self._move_to_end(key)
        return value

    def put(self, key: int, value: int) -> None:
        self._move_to_end(key)
        self._cache[key] = value
        if self._isFull:
            lru = self._usage.pop(0)
            if lru in self._cache:
                self._cache.pop(lru)
        

cache = LRUCache(2)
cache.put(2, 1)
print(cache.get(2))
cache.put(2, 2) 
print(cache.get(2))
cache.put(1, 1)
cache.put(4, 1) 