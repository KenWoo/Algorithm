from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        size = 0
        tmp = ListNode(0)
        tmp.next = head
        cur = tmp
        while cur.next:
            size += 1
            cur = cur.next
        cur.next = head
        for i in range(size-k % size):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        return new_head


if __name__ == "__main__":
    pass
