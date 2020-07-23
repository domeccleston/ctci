"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

NOTES

Enqueue: add an item to our data structure
Dequeue: remove the least-recently-added element

qvs.push(1) -> s1: [1] | s2: [1]
qvs.push(2) -> s1: [1, 2] | s2: [2, 1]
qvs.push(3) -> s1: [] | s2: [2, 1] -> s1: [1, 2, 3] | s2: [] -> s1: [] | s2: [3, 2, 1]

"""
class Stack:
    def __init__(self):
        self.data = []
    
    def pop(self):
        return self.data.pop()

    def push(self, i):
        self.data.append(i)
        return self.data

    def peek(self):
        return self.data[0];

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def __repr__(self):
        return str(self.data)

class QueueViaStacks:

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def push(self, item):
        if self.stack_2.size() == 0:
            self.stack_2.push(item)
        else:
            while self.stack_2.size() > 0:
                head = self.stack_2.pop()
                self.stack_1.push(head)
            self.stack_1.push(item)
            while self.stack_1.size() > 0:
                head = self.stack_1.pop()
                self.stack_2.push(head)

    def pop(self):
        return self.stack_2.pop()

    def __repr__(self):
        s = ''
        s += f'Stack 1: {self.stack_1.data} '
        s += f'Stack 2: {self.stack_2.data}'
        return s


qvs = QueueViaStacks()
qvs.push(1)
qvs.push(2)
qvs.push(3)
print(qvs.pop())
print(qvs.pop())
print(qvs.pop())
qvs.push(4)
qvs.push(5)
qvs.push(6)
print(qvs)
print(qvs.pop())