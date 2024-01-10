import pytest

from src.queue import Node, Queue


@pytest.fixture
def test_node():
    return Node(1, 2)


@pytest.fixture
def ex_queue():
    return Queue()


def test_node_init(test_node):
    assert test_node.data == 1
    assert test_node.next_node == 2


def test_queue_str(ex_queue):
    ex_queue.enqueue('data1')
    ex_queue.enqueue('data2')
    ex_queue.enqueue('data3')
    assert str(ex_queue) == "data1\ndata2\ndata3"


def test_queue_enqueue(ex_queue):
    ex_queue.enqueue('data1')
    ex_queue.enqueue('data2')
    ex_queue.enqueue('data3')

    assert ex_queue.head.data == 'data1'
    assert ex_queue.head.next_node.data == 'data2'
    assert ex_queue.tail.data == 'data3'
    assert ex_queue.tail.next_node is None


def test_queue_dequeue(ex_queue):
    ex_queue.enqueue('data1')
    ex_queue.enqueue('data2')

    assert ex_queue.dequeue() == "data1"
    assert ex_queue.dequeue() == "data2"
    assert ex_queue.dequeue() is None
