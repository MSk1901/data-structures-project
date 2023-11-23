import pytest

from src.linked_list import Node, LinkedList


@pytest.fixture
def test_node():
    return Node(1, None)


@pytest.fixture
def ex_list():
    return LinkedList()


def test_node_init(test_node):
    assert test_node.data == 1
    assert test_node.next_node is None


def test_linked_list_insert_beginning(ex_list):
    ex_list.insert_beginning({'id': 1})
    ex_list.insert_at_end({'id': 2})
    ex_list.insert_at_end({'id': 3})
    ex_list.insert_beginning({'id': 0})

    assert ex_list.head.data == {'id': 0}
    assert str(ex_list) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
