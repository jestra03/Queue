# Queue Linked [Data Structures]
# Joshua Estrada

class Node:
    def __init__(self, item):
        self.item = item  # save data
        self.next = None  # initialize next ref


class Queue:
    def __init__(self, capacity):
        # Implements an array-based, efficient first-in first-out Abstract Data Type
        self.capacity = capacity  # set node limit
        self.front = None  # set front ref
        self.back = None  # set back ref
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
        if self.is_empty():
            self.front = Node(item)
        if self.num_items == 1:
            self.back = Node(item)
            self.front.next = self.back
        if self.num_items > 1:
            new_back = Node(item)
            self.back.next = new_back
            self.back = new_back
        self.num_items += 1
        # enqueue item to back ref of queue (0(1) performance)

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        removed = self.front.item
        new_front = self.front.next
        self.front = new_front
        self.num_items -= 1
        return removed  # return dequeued item
        # dequeue item at the front ref of queue (0(1) performance)

    def size(self):
        return self.num_items
        # return number of items in stack (0(1) performance)
