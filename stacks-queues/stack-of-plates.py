"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. 

SetOfStacks should be composed of several stacks and should create a new stack
once the previous one exceeds capacity. 

SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).

FOLLOW UP

Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)

class SetOfStacks:
    def __init__(self, maxlength):
        self.stacks = []
        self.index = 0
        self.maxlength = maxlength

    def push(self, item):
        if len(self.stacks) == 0:
            self.stacks.append(Stack())
        if self.stacks[self.index].size() == self.maxlength:
            self.index += 1
            self.stacks.append(Stack())

        self.stacks[self.index].push(item)

    def pop(self):
        if len(self.stacks) == 0:
            raise Exception("Cannot pop from empty stack!")
        if self.stacks[self.index].size() == 0:
            del self.stacks[self.index]
            self.index -= 1
        return self.stacks[self.index].pop()

    def popAt(self, index):
        return self.stacks[index].pop()

    def _print(self):
        for i in self.stacks:
            print(i)

        

sos = SetOfStacks(3)
sos.push(1)
sos.push(2)
sos.push(3)
sos.push(4)
sos.push(5)
sos.push(6)
sos.push(7)
sos.push(8)
sos.push(9)
sos._print()