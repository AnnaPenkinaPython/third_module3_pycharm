class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_beginning(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)

    def to_list(self):
        list_of_contents = []
        current = self.head
        while current is not None:
            list_of_contents.append(current.data)
            current = current.next_node
        return list_of_contents

    def get_data_by_id(self, id):
        list_of_contents = self.to_list()
        for item in list_of_contents:
            try:
                if type(item) == dict:
                    if item['id'] == id:
                        return item
                else:
                    raise TypeError
            except TypeError:
                print('Данные не являются словарем или в словаре нет id')
