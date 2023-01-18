# Queue Array [Data Structures]
# Joshua Estrada

class Queue:
    def __init__(self, capacity):
        # Implements an array-based, efficient first-in first-out Abstract Data Type
        self.capacity = capacity  # initialize counter
        self.items = [None] * capacity  # initialize array and allocate memory
        self.front = 0  # initialize front ref index
        self.back = 0  # initialize back ref index
        self.num_items = 0  # set item counter

    def is_empty(self):
        return self.num_items == 0
        # checks if queue is empty (0(1) performance)

    def is_full(self):
        return self.num_items == self.capacity
        # checks if queue is full (0(1) performance)

    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        self.items[self.back] = item
        if self.back == self.capacity - 1:  # max idx reached
            self.back = 0  # reset back idx to 0
        else:
            self.back += 1
        self.num_items += 1
        # enqueue item to back of queue (0(1) performance)

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        removed = self.items[self.front]
        if self.front == self.capacity - 1:  # reset front index
            self.front = 0
        else:
            self.front += 1
        self.num_items -= 1
        return removed  # returns dequeued item
        # dequeue item at the front of queue (0(1) performance)

    def size(self):
        return self.num_items
        # return number of items in stack (0(1) performance)
