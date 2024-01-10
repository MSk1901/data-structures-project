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
    assert (str(ex_list) ==
            "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")


def test_linked_list_to_list(ex_list):
    ex_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ex_list.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ex_list.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ex_list.insert_beginning({'id': 0, 'username': 'serebro'})

    lst = ex_list.to_list()

    assert lst[0] == {'id': 0, 'username': 'serebro'}
    assert lst[1] == {'id': 1, 'username': 'lazzy508509'}
    assert lst[2] == {'id': 2, 'username': 'mik.roz'}
    assert lst[3] == {'id': 3, 'username': 'mosh_s'}


def test_linked_list_get_data_by_id(ex_list):
    ex_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ex_list.insert_at_end({'id': 2, 'username': 'mosh_s'})

    assert ex_list.get_data_by_id(2) == {'id': 2, 'username': 'mosh_s'}


def test_linked_list_get_data_by_id_invalid_data(ex_list, capsys):
    ex_list.insert_beginning('idusername')
    ex_list.insert_at_end([1, 2, 3])

    ex_list.get_data_by_id([1, 2, 3])

    captured = capsys.readouterr()

    assert (captured.out.strip()
            == """Данные не являются словарем или в словаре нет id.
Данные не являются словарем или в словаре нет id.""")
