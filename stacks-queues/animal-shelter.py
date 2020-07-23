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

class Animal:
    def __init__(self):
        self.order = 0

    def setOrder(self, order):
        self.order = order

    def isOlderThan(self, animal):
        return self.order > animal.order

class Dog(Animal):
    def __init__(self):
        super().__init__()

class Cat(Animal):
    def __init__(self):
        super().__init__()

class AnimalQueue:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0

    def enqueue(self, animal):
        animal.setOrder(self.order)
        self.order += 1
        if isinstance(animal, Cat):
            self.cats.append(animal)
        elif isinstance(animal, Dog):
            self.dogs.append(animal)
        else:
            raise TypeError("Dogs or cats only")

    def dequeueAny(self):
        if len(dogs) == 0:
            return self.dequeueCats()
        elif len(cats) == 0:
            return self.dequeueDogs()
        
        oldest_dog = list(dogs)[0]
        oldest_cat = list(cats)[0]

        if dog.isOlderThan(cat):
            return dequeueDogs()
        else:
            return dequeueCats()

    def dequeueDogs(self):
        return self.dogs.popleft()

    def dequeueCats(self):
        return self.cats.popleft()

    def __repr__(self):
        s = ''
        s += 'Dogs: ' + str(list(self.dogs)) + '\n'
        s += 'Cats: ' + str(list(self.cats))
        return s
    


a = AnimalQueue()
d1 = Dog()
c1 = Cat()
c2 = Cat()
a.enqueue(d1)
a.enqueue(c1)
a.enqueue(c2)
print(a.dequeueDogs())
print(a)