class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __int__(self, top=None):
        self.top = top

    @property
    def top(self):
        """"добавляет данные в стэк"""
        return self.top

    @top.setter
    def top(self, value):
        if isinstance(value, Node):
            self.top = value
        else:
            self.top = Node(value)




