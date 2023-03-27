import unittest
from main import *
from custom_queue import Queue
from custom_queue import *
from io import StringIO
from linked_list import LinkedList, Node, ll
from contextlib import redirect_stdout

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


class Linked_listtest(unittest.TestCase):

    def test_print_ll(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        expected_output = "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
        f = StringIO()
        with redirect_stdout(f):
            ll.print_ll()
        self.assertEqual(f.getvalue().strip(), expected_output)

        def test_to_list(self):
            ll = LinkedList()
            ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
            ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
            ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
            ll.insert_beginning({'id': 0, 'username': 'serebro'})
            lst = ll.to_list()
            self.assertEqual(len(lst), 4)
            self.assertEqual(lst[0]['id'], 0)
            self.assertEqual(lst[3]['id'], 3)

        def test_get_data_by_id(self):
            ll = LinkedList()
            ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
            ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
            self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})
            self.assertEqual(ll.get_data_by_id(3), None)
