class Stack:
    def __init__(data=[]):
        self.data = data
    
    def pop(self, i):
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
