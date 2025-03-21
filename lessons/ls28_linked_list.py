"""Simple linked list example."""

from __future__ import annotations

from typing import Optional


class Node:
    """Single linked list Node."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Constructor."""
        self.data = data
        self.next = next

    
def count(head: Optional[Node]) -> int:
    """Counts up the length of a linked list."""
    if head is None:
        return 0
    else:
        return 1 + count(head.next)


third_node: Node = Node(3, None)
second_node: Node = Node(2, third_node)
a_node: Node = Node(1, second_node)

print(a_node.data)
print(a_node.next.next.next)
print(third_node.data)
print(second_node.next.data)
print(a_node.next.next.data)
print(count(a_node))