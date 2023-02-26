import unittest
from main import *
"""тесты"""
n1 = Node(5, None)
n2 = Node('a', n1)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')

stack.pop()



class TestMain(unittest.TestCase):



    def test_pop(self):
        self.assertEqual(stack.top.data, 'data2')

