import sys

"""
minheap:
    - complete binary tree (totally filled, with possible exception of rightmost element)
    - ordered in descending order: each node is smaller than both of its children
    - two main operations:
        - insert:
            - insert the new node as the rightmost node
            - while node < parent, swap node and parent
        - extract minimum node:
            - the minimum node is at the top of the min heap
            - swap the root node with the rightmost node
            - while the new root node is larger than its children, swap it with whichever child is smaller

we can easily map a min heap to an array arr, where a node stored at index k has its left child at arr[2k + 1] and its right at arr[2k + 2]

time complexity:
    - get min: O(log n): we can check the minimum element in O(1) time, but if we remove it we must reorder the heap
    - insert: O(log n): this refers to the worst case, where we need to traverse up to the top of the tree to insert a new minimum element
"""

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2
    
    def leftChild(self, pos):
        return pos * 2

    def rightChild(self, pos):
        return (pos * 2) + 1
    
    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        else:
            return False

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
                self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        
    def Print(self):
        print("HEAP: " + str(self.Heap))
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT: " + str(self.Heap[i]) +     " LEFT CHILD: "+
                                str(self.Heap[2 * i]) + " RIGHT CHILD: "+
                                str(self.Heap[2 * i + 1]))
        print('\n')

    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped

minheap = MinHeap(10)
minheap.insert(4)
minheap.Print()
minheap.insert(50)
minheap.Print()
minheap.insert(7)
minheap.Print()
minheap.insert(55)
minheap.insert(90)
minheap.insert(87)
minheap.minHeap()
minheap.Print()
minheap.remove()
