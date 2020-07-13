"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

1 -> s1: 1 | s2: [1]
2 -> s2: 1, 2 | s2: [2, 1]
3 -> s1: 1, 2, 3 | s2: [3, 2, 1]

4 -> s1: 4 | s2: 4
2 -> s1: 4, 2 | s2: 4, 2  ::: 2 < 4, so push to s2
3 -> s1: 4, 2, 3 | s2: 4, 3, 2 ::: 3 > 2, so pop off 2 and store in temp. Look at head. 4 > 3, so push to s2. Add temp back in.
1 -> s1: 4, 3, 2, 1 | s2: 4, 3, 2 ::: push 1

"""

class SortedStack:
    def __init__(self):
        self.stack = []
        self.temp = []

    def recurse(stack, temp, head, item):
        if len(stack) == 0:
            return stack
        
    
    def push(self, item):
        if not isinstance(item, int):
            raise ValueError("Integer input only")
        if self.isEmpty() or item <= self.peep():
            self.stack.append(item)
        else:
            while self.peep() is not None and item > self.peep():
                head = self.stack.pop()
                self.temp.append(head)
            self.stack.append(item)
            while len(self.temp) > 0:
                t_head = self.temp.pop()
                self.stack.append(t_head)
            
        return self.stack

    def pop(self):
        return self.stack.pop()
    def peep(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0

ss = SortedStack()
print(ss.push(4))
print(ss.push(2))
print(ss.push(3))
print(ss.push(1))
print(ss.push(5))
print(ss.push(0))
print(ss.push(5))
print(ss.push(5))
print(ss.push(-10))
print(ss.push(10000))