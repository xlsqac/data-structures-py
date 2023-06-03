from typing import Any

from .linked_list import LinkedList
from .node import DoublyNode
from .singly_linked_list import SinglyLinkedList


class DoublyLinkedList(SinglyLinkedList):
    """双向链表 0<>1<>2>None"""

    def add(self, item: Any) -> None:
        if self.is_empty():
            next = prev = None
            node = DoublyNode(item, next, prev)
        else:
            next = self._head
            prev = None
            node = DoublyNode(item, next, prev)
            # 修改当前头结点的值
            self._head.prev = node
        self._head = node

    def append(self, item: Any) -> None:
        if self.is_empty():
            next = prev = None
            node = DoublyNode(item, next, prev)
            self._head = node
        else:
            current = self._head
            prev = None
            while current.next is not None:
                prev = current
                current = current.next
            next = None
            node = DoublyNode(item, next, prev)
            current.next = node

    def insert(self, position: int, item: Any) -> None:
        if position == 0:
            self.add(item)
        else:
            current = self._head
            prev = None
            count = 0
            while count < position - 1:
                count += 1
                prev = current
                current = current.next

            node = DoublyNode(item, current.next, prev)
            current.next = node

    def search(self, item: Any) -> bool:
        if self.is_empty():
            return False

        current = self._head
        while current:
            if current.item == item:
                return True
            current = current.next

    def remove(self, item: Any) -> None:
        current = self._head
        prev = None
        while current:
            if current.item == item:
                # 删除头结点
                if prev is None:
                    self._head = current.next
                    self._head.prev = prev
                # 删除尾结点
                elif current.next is None:
                    current.prev.next = None
                else:
                    prev.next = current.next
                    current.next.prev = prev

            prev = current
            current = current.next

    def _to_list(self, is_print: bool = False) -> list:
        output = []
        current = self._head
        while current:
            if is_print:
                print(current.item)

            output.append(current.item)
            current = current.next
        return output
