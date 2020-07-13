"""
Animal Shelter: An animal shelter, which holds only dogs and cats, 
operates on a strictly "first in, first out" basis. People must adopt either the "oldest" 
(based on arrival time) of all animals at the shelter, or they can select whether they would prefer
a dog or a cat (and will receive the oldest animal of that type). They cannot select which 
specific animal they would like. Create the data structures to maintain this system and
implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use
the built-in Linked list data structure.


queue: [cat, dog, cat, dog]
temp:  []

dequeueDog() -> [cat, dog, cat, dog] | [] -> [dog, cat, dog] | [cat] -> [cat, dog] | [cat] -> [] -> [cat, cat, dog] | []

dequeueDog() -> [cat, cat, cat, dog, cat] | []

pseudo:

- while len > 0:
    - check head
    - if of type sought, concat temp to queue and return head
    - else, push to temp
"""

from collections import deque

class AnimalShelter:
    def __init__(self):
        self.queue = deque()
        self.temp = []

    def size(self):
        return len(self.queue)
    
    def dequeueAny(self):
        return self.queue.popleft()

    def _dequeueType(self, type):
        head = self.dequeueAny()
        if self.size() == 0:
            self.queue.extend(self.temp)
        elif head == type:
            self.queue.extendleft(self.temp)
            self.temp = []
            return head
        else:
            self.temp.append(head)
            return self._dequeueType(type)

    def dequeueDog(self):
        return self._dequeueType('dog')

    def dequeueCat(self):
        return self._dequeueType('cat')

    def enqueue(self, item):
        self.queue.append(item)

    def __repr__(self):
        return str(list(self.queue))


a = AnimalShelter()
a.enqueue('dog')
a.enqueue('dog')
a.enqueue('cat')
a.enqueue('dog')
a.enqueue('cat')
print(a)
print(a.dequeueCat())
print(a)