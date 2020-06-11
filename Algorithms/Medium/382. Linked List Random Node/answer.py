from typing import List
from random import randint


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        reservoir = -1
        cur, n = self.head, 0
        while cur:
            reservoir = cur.val if randint(1, n+1) == 1 else reservoir
            cur, n = cur.next, n+1
        return reservoir


if __name__ == "__main__":
    pass
