import unittest
from main import *
from custom_queue import Queue
from custom_queue import *
"""тесты"""
n1 = Node(5, None)
n2 = Node('a', n1)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')

stack.pop()



class TestMain(unittest.TestCase):

        def test_Node(self):
            self.assertEqual(n1.data, 5)
            self.assertEqual(n2.data, 'a')
            self.assertEqual(n1.data, 5)
            self.assertEqual(n1.next_node, None)

        def test_Stack(self):
            self.assertEqual(stack.top.data, 'data2')
            self.assertEqual(stack.top.next_node.data, 'data1')
            self.assertEqual(stack.top.next_node.next_node, None)

        def test_pop(self):
            self.assertEqual(stack.top.data, 'data2')


class TestQueue(unittest.TestCase):
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    def test_queue(self):
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')

    def test_dequeue(self):
        self.assertEqual(queue.dequeue, 'data1')
        self.assertEqual(queue.dequeue, 'data2')
        self.assertEqual(queue.dequeue, 'data3')

