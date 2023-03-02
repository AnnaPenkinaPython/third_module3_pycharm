class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self, start=None, stop=None):
        self.start = start
        self.stop = stop


    def enqueue(self, data):
        new_node = Node(data=value)
        if self.start is None:
            self.start = new_node
            self.stop = new_node
        else:
            self.stop.next_node = new_node
            self.stop = new_node
