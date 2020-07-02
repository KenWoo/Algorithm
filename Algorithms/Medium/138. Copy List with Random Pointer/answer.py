from typing import List

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        p = head
        while p:
            node = Node(p.val)
            node.next = p.next
            p.next = node
            p = node.next
        p = head
        while p:
            p.next.random = None if not p.random else p.random.next
            p = p.next.next
        newhead = head.next
        p = head.next
        while p:
            head.next = p.next
            head = head.next
            p.next = None if not head else head.next
            p = p.next
        return newhead

if __name__ == "__main__":
    pass