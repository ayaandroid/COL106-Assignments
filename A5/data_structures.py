class Node:
    def __init__(self, element, next = None):
        self.element = element
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    
    def insert_last(self, e):
        new = Node(e)
        if self.is_empty(): self.head = new
        else: self.tail.next = new
        self.tail = new

    def remove_first(self):
        if self.is_empty(): raise Exception("List is empty")
        e = self.head.element
        if self.head.next is None: self.tail = None
        self.head = self.head.next
        return e
    
class Queue:
    def __init__(self):
        self.data = LinkedList()

    def enqueue(self, e):
        self.data.insert_last(e)

    def is_empty(self):
        return self.data.is_empty()
    
    def dequeue(self):
        if self.is_empty(): raise Exception("Queue is empty")
        return self.data.remove_first()

class PriorityQueue:
    def __init__(self, comparator):
        self.data = []
        self.comp = comparator

    def is_empty(self):
        return len(self.data) == 0
    
    def insert(self, x):
        self.data.append(x)
        self._upheap(len(self.data) - 1)

    def _upheap(self, i):
        while i != 0:
            parent = (i-1)//2
            if self.comp(self.data[i], self.data[parent]):
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else: break

    def remove_min(self):
        if self.is_empty(): raise Exception('Queue is empty')
        min = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self._downheap(0)
        return min
    
    def _downheap(self, i):
        n = len(self.data)
        j = i
        while True:
            left = 2*j + 1
            if left >= n: break
            smaller_child = left
            right = 2*j + 2
            if right < n and self.comp(self.data[right], self.data[left]): 
                smaller_child = right
            if self.comp(self.data[smaller_child], self.data[j]):
                self.data[smaller_child], self.data[j] = self.data[j], self.data[smaller_child]
                j = smaller_child
            else: break