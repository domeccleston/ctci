
class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0
	
	def push(self, key, value):
		''' Wrap a value in a node and add to the head of the linked list '''
		new_node = Node(key, value)
		new_node.next = self.head
		if not self.head and not self.tail:
			self.head = new_node
			self.tail = new_node
		if self.head is not None:
			self.head.prev = new_node
		self.head = new_node
		self.length += 1

	def delete(self, node: Node):
		if node == None:
			return
		if self.head == node:
			self.head = self.head.next
		if self.tail == node:
			self.tail = self.tail.prev
		if node.next is not None:
			node.next.prev = node.prev
		if node.prev is not None:
			node.prev.next = node.next
		self.length -= 1

	def print_list(self):
		i = self.head
		print(f"Length: {self.length}")
		while i != None:
			if i == self.head:
				print(f"Head: {i.key} : {i.value}")
			elif i == self.tail:
				print(f"Tail: {i.key} : {i.value}")
			else:
				print(f"{i.key} : {i.value}")
			i = i.next
		print("\n")

class LRUCache:
	def __init__(self, limit=3):
		self.limit = limit
		self.storage = {}
		self.entries = DoublyLinkedList()

	def get(self, key):
		if key in self.storage:
			value_node = self.storage[key]
			value = value_node.value
			self.entries.delete(value_node)
			self.entries.push(key, value)
			return value
		else:
			return None

	def set(self, key, value):
		if key not in self.storage:
			if self.entries.length < self.limit:
				self.entries.push(key, value)
				self.storage[key] = self.entries.head
			else:
				LRU = self.entries.tail
				print(LRU.key, LRU.value)
				del self.storage[LRU.key]
				self.entries.delete(LRU)
				self.entries.push(key, value)
				self.storage[key] = self.entries.head
		elif key in self.storage:
			value_node = self.storage[key]
			del self.storage[value_node.key]
			self.entries.delete(value_node)
			self.entries.push(key, value)
			self.storage[key] = self.entries.head


	def print_cache(self):
		for k, v in self.storage.items():
			print(f"{k}: ({v}, {v.value})")
		self.entries.print_list()

lru = LRUCache()
lru.set(1, 1)
lru.set(2, 2)
lru.set(3, 3)
lru.get(2)
lru.set(4, 4)

lru.print_cache()