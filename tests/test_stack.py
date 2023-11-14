"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest

from src.stack import Node, Stack


@pytest.fixture
def test_node():
    return Node(1, 2)


@pytest.fixture
def stack():
    return Stack()


def test_node_init(test_node):
    assert test_node.data == 1
    assert test_node.next_node == 2


def test_stack_init(stack):
    assert stack.top is None


def test_stack_push(stack):
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    assert stack.top.data == "data3"
    assert stack.top.next_node.data == "data2"


def test_stack_pop_not_empty(stack):
    stack.push('data1')
    stack.push('data2')
    stack.pop()

    assert stack.top.data == 'data1'


def test_stack_pop_empty(stack):
    assert stack.pop() is None
