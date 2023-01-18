# Queue Tests [Data Structures]
# Joshua Estrada

import unittest
from queue_array import Queue
# from queue_linked import Queue


class TestLab1(unittest.TestCase):
    def test_queue(self):
        q = Queue(5)  # sets Queue and it's max capacity
        self.assertTrue(q.is_empty())  # check if queue is empty (no items)
        self.assertFalse(q.is_full())  # check if queue is full (items at max capacity)
        q.enqueue('thing')  # enqueue first item to queue (which is also in the back)
        self.assertEqual(q.size(), 1)  # check if number of items in queue is one
        self.assertFalse(q.is_empty())  # verify that queue is not empty
        q.dequeue()  # dequeue front item in queue
        self.assertTrue(q.is_empty())  # check if queue is empty
        self.assertEqual(q.size(), 0)  # check for no items

    def test_order(self):
        q = Queue(8)
        for i in range(8):
            q.enqueue(i)
        # 0 1 2 3 4 5 6 7

        self.assertEqual(q.size(), 8)
        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.dequeue(), 1)
        # X X 2 3 4 5 6 7

        q.enqueue(9)
        q.enqueue(10)
        # 9 10 2 3 4 5 6 7

        for i in range(6):
            q.dequeue()
        # 9 10 X X X X X X

        self.assertEqual(q.size(), 2)
        q.dequeue()
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.size(), 0)
        # tests if array queue dequeues from the front enqueue from the back
        # tests if linked queue dequeues front node and enqueues new node to back

        # testcase tests if array queue can wrap around n(1)

    def test_dequeue(self):
        q = Queue(10)
        self.assertTrue(q.is_empty())
        self.assertEqual(q.size(), 0)
        for i in range(10):
            q.enqueue(i + 1)
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 10)
        q.dequeue()  # remove 1
        self.assertEqual(q.dequeue(), 2)  # remove 2
        self.assertFalse(q.is_full())
        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), 8)

    def test_index_error(self):
        q = Queue(3)
        self.assertRaises(IndexError, q.dequeue)
        for i in range(3):
            q.enqueue(i)
        self.assertRaises(IndexError, q.enqueue, 3)

    def test_full_stack(self):
        q = Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 5)
        self.assertRaises(IndexError, q.enqueue, 0)

    def test_empty_stack(self):
        q = Queue(5)
        self.assertTrue(q.is_empty())
        self.assertEqual(q.size(), 0)
        self.assertRaises(IndexError, q.dequeue)

    def test_none(self):
        q = Queue(3)
        q.enqueue(None)
        self.assertEqual(q.size(), 1)
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_string(self):
        q = Queue(5)
        q.enqueue('hello')
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 'hello')
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue('t1')
        q.enqueue('t2')
        q.enqueue('t3')
        q.enqueue('t4')
        q.enqueue('t5')
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 5)
        q.dequeue()
        self.assertEqual(q.dequeue(), 't2')
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 3)

    def test_empty_queue(self):
        q = Queue(0)
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertRaises(IndexError, q.dequeue)
        self.assertRaises(IndexError, q.enqueue, 1)

    def test_queue_of_one(self):
        q = Queue(1)
        self.assertEqual(q.size(), 0)
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)

    def test_queue_of_two(self):
        q = Queue(2)
        self.assertEqual(q.size(), 0)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 1)
        q.enqueue(0)
        self.assertFalse(q.is_full())
        self.assertFalse(q.is_empty())
        q.enqueue(1)
        self.assertTrue(q.is_full())
        self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.dequeue(), 1)
        self.assertFalse(q.is_full())
        self.assertTrue(q.is_empty())
        self.assertEqual(q.size(), 0)


if __name__ == '__main__': 
    unittest.main()
