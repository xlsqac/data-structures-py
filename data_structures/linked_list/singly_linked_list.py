from typing import Any, Union

from .linked_list import LinkedList
from .node import Node


class SinglyLinkedList(LinkedList):
    """单向链表 0>1>2>None"""

    def length(self) -> int:
        """链表数量 O(n)"""
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item: Any) -> None:
        """增加结点到末尾，平均 O(n)，最好 O(1) 空链表"""
        # 生成新结点
        next = None
        node = Node(item, next)
        # 链表为空时，头结点和尾结点都为新添加的结点
        if self.is_empty():
            self._head = node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = node

    def add(self, item: Any) -> None:
        """增加结点到表头 O(1)"""
        # 根据表是否为空来确定 next 的值
        if self.is_empty():
            next = None
        else:
            next = self._head

        node = Node(item, next)
        self._head = node

    def insert(self, position: int, item: Any) -> None:
        """插入结点到指定位置，平均时间复杂度 O(n)，最好情况往开头插入 O(1)"""
        # 插入位置为 0 的时候直接 add
        if position == 0:
            self.add(item)
        else:
            # 其他位置，需要从头结点开始遍历
            previous = self._head
            count = 0
            while count < position - 1:
                count += 1
                previous = previous.next
            node = Node(item, previous.next)
            previous.next = node

    def remove(self, item: Any) -> None:
        """删除指定结点 O(n)"""
        current = self._head
        previous = None
        while current is not None:
            if current.item == item:
                # 说明删除的是头结点
                if previous is None:
                    self._head = current.next
                else:
                    previous.next = current.next
                break
            previous = current
            current = current.next

    def search(self, item: Any) -> bool:
        """查找指定结点是否存在 O(n)"""
        current = self._head
        while current is not None:
            if current.item == item:
                return True
            current = current.next
        return False

    def _to_list(self, is_print: bool = False) -> list:
        output = []
        current = self._head
        while current is not None:
            if is_print:
                print(current.item)

            output.append(current.item)
            current = current.next
        return output

    def move_to_head(self, node: Node) -> None:
        """
        将指定结点移动到头部
        :param node: Node type，要移动的结点
        :return:
        """
