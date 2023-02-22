"""Узел нод для с двумя атрибутами, poetry, unittest"""


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


"""Узел стак  """


class Stack:
    def __init__(self):
        self.top = None

    """Добавление данных в стак"""

    def push(self, value):
        new_node = Node(data=value)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        remove = self.top
        self.top = self.top.next_node
        return remove.data







