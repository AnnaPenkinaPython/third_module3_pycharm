import pytest
from main import Node, Stack


@pytest.fixture()
def node_10():
    return Node(20)

def test_node_init():
    node = Node(10)
    assert node.data == 10
    assert node.next_node is None


def test_node_next_nove():
    """проверка next_node ссылается на узел"""
    node1 = Node(10)
    node2 = Node(229, node1)
    assert node2.next_node is node1
