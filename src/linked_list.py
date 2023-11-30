class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь)
        и добавляет узел с этими данными в начало связанного списка"""

        new_node = Node(data, None)
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь)
        и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data, None)
        current = self.head
        if not self.head:
            self.head = new_node
        else:
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        """Возвращает список с данными,
        содержащимися в односвязном списке LinkedList"""
        current = self.head
        data_list = []
        while current:
            data_list.append(current.data)
            current = current.next_node
        return data_list
