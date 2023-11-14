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
        self.all.append(data)
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
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        return "\n".join(self.all)
