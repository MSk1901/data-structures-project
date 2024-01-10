class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.all = []

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        obj = Node(data, None)
        if not self.head:
            self.head = obj
            self.tail = self.head
        else:
            self.tail.next_node = obj
            self.tail = obj

    def dequeue(self):
        """
        Метод для удаления элемента из очереди.
        Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head:
            data = self.head.data
            self.head = self.head.next_node
            return data
        return None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        current = self.head
        queue_str = ""
        while current:
            queue_str += str(current.data) + "\n"
            current = current.next_node
        return queue_str.strip()
