from __future__ import annotations
from typing import Any, Union


class Node:
    def __init__(self, item: Any, next: Union[Node, None]) -> None:
        self.item = item
        self.next = next
