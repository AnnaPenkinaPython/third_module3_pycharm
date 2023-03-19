class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        data = []

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_beginning(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next_node

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next_node is not None:
                n = n.next_node
            n.next_node = next_node



