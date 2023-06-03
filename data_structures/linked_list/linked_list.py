from typing import Any


class LinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        """链表是否为空"""
        return self._head is None

    def length(self) -> int:
        """链表数量"""
        raise NotImplementedError

    def search(self, item: Any) -> bool:
        """
        查找值是否在链表内

        :param item: type Any，要查找的值
        :return: bool，是否存在
        """
        raise NotImplementedError

    def _to_list(self, is_print: bool = False) -> list:
        """
        将链表转成 list

        :param is_print: type bool，控制是否需要打印每一个值
        :return output: type list，链表转成的 list
        """
        raise NotImplementedError

    def travel(self) -> None:
        """
        遍历链表，通过 _to_list(is_print=True) 实现，is_print 会控制转 list 时，是否打印值
        """
        self._to_list(is_print=True)

    def to_list(self) -> list:
        """链表转 list"""
        return self._to_list()

    def add(self, item: Any) -> None:
        """
        在头结点插入值，时间复杂度 O(1)

        :param item: type Any，要插入的值
        :return:
        """
        print(item)
        raise NotImplementedError

    def append(self, item: Any) -> None:
        """
        在尾结点插入值，时间复杂度 O(n)

        :param item: type Any，要插入的值
        :return:
        """
        raise NotImplementedError

    def insert(self, position: int, item: Any) -> None:
        """
        指定位置插入值，在头结点插入时为最好时间复杂度 O(1)，在尾结点插入时为最坏时间复杂度 O(n)，平均时间复杂度 O(n)

        :param position: type int，要插入的位置
        :param item: type Any，要插入的值
        :return:
        """
        raise NotImplementedError

    def remove(self, item: Any) -> None:
        """
        删除指定值，删除头结点为最好时间复杂度 O(1)，删除尾结点为最坏时间复杂度 O(n)，平均时间复杂度 O(n)
        :param item: type Any，要删除的值
        :return:
        """
        raise NotImplementedError

    @property
    def head(self):
        return self._head
