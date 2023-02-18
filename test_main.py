import unittest
from main import *
"""тесты"""
n1 = Node(5, None)
n2 = Node('a', n1)

stack = Stack()
stack.top('data1')
stack.top('data2')
stack.top('data3')


class TestMain(unittest.TestCase):

    def test_Node(self):
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n1.data, 5)
        self.assertEqual(n1.next_node, None)

    def test_Stack(self):
        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(stack.top.next_node.next_node.next_node, None)