import os
import sys
from typing import Any, Union

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from node import Node
from singly_linked_list.singly_linked_list import SinglyLinkedList

TRAVEL = "travel"  # 遍历的标志，控制 _travel 函数是否打印 item


class SinglyCycleLinkedList(SinglyLinkedList):
    """
    单向循环链表，尾结点指向头结点
    在单向链表的基础上修改 add，append，insert，remove, length 等操作
    """

    def length(self):
        if self.is_empty():
            return 0

        count = 1
        current = self._head
        # 只有一个元素
        if current.next is None:
            return count

        while current.next is not self._head:
            count += 1
            current = current.next
        return count

    def add(self, item: Any) -> None:
        """在链表开头增加结点"""
        if self.is_empty():
            node = Node(item, None)
        else:
            node = Node(item, self._head)
            current = self._head
            # 找到尾结点
            while True:
                # 只有一个结点
                if current.next is None:
                    current.next = node
                    break
                elif current.next == self._head:
                    current.next = node
                    break

                current = current.next

            # 将头结点插入链表
        self._head = node

    def append(self, item: Any) -> None:
        """在链表末尾增加结点"""
        if self.is_empty():
            node = Node(item, None)
            self._head = node
        else:
            node = Node(item, self._head)
            current = self._head
            # 找到之前的尾结点
            while True:
                # 链表中只有一个结点时
                if current.next is None:
                    current.next = node
                    break
                # 单向循环链表尾结点指向的是头结点
                elif current.next == self._head:
                    current.next = node
                    break

                # 将指针交给下一个结点，进行下一次循环
                current = current.next

    def remove(self, item: Any) -> None:
        current = self._head
        # 要删除的结点为头结点
        if current.item == item:
            # 找到尾结点
            while True:
                if current.next is self._head:
                    current.next = self._head.next
                    self._head = current.next
                    break
                current = current.next
        else:
            previous = None

            while True:
                if current.item == item and previous:
                    previous.next = current.next
                    break

                # 控制循环退出，防止传入一个不存在的值，导致死循环
                if current.next in (
                    self._head,
                    None,
                ):
                    break

                previous = current
                current = current.next

    def _travel(self, option: Union[str, None] = None) -> list:
        output = []
        current = self._head
        while True:
            output.append(current.item)
            if option == TRAVEL:
                print(current.item)
            # 尾结点或只有一个结点
            if current.next == self._head or current.next is None:
                break
            else:
                current = current.next
        return output

    def to_list(self) -> list:
        """链表转换成列表"""
        return self._travel()

    def travel(self) -> None:
        """遍历链表"""
        self._travel(option=TRAVEL)
