from __future__ import annotations

from typing import Any, Union


class Node:
    def __init__(self, item: Any, next: Node | None) -> None:
        self.item = item
        self.next = next


class DoublyNode:
    def __init__(
        self,
        item: Any,
        next: DoublyNode | None,
        prev: DoublyNode | None,
    ) -> None:
        self.item = item
        self.next = next
        self.prev = prev
