"""基于链表实现的 LRU 策略"""
from typing import Any

from .singly_linked_list import SinglyLinkedList


class LRUCache:
    def __init__(self, max_length: int):
        self.linked_list = SinglyLinkedList()
        self.max_length = max_length

    def _is_full(self) -> bool:
        return self.linked_list.length() >= self.max_length

    def get(self, key: str):
        current = self.linked_list.head
        while current:
            if key in current.item:
                # 访问完之后要把 key 放到头结点
                self.linked_list.move_to_head(current)
                return current.item[key]
            current = current.next
        return -1

    def put(self, key: str, value: str):
        pass
