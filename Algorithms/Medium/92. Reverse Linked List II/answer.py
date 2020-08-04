from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        tmp, N = ListNode(0), n - m
        tmp.next = head
        prev, cur = tmp, tmp.next
        while m > 1:
            prev, cur = cur, cur.next
            m -= 1
        last, first = prev, cur
        while cur and N >= 0:
            cur.next, prev, cur = prev, cur, cur.next
            N -= 1
        last.next, first.next = prev, cur
        return tmp.next

if __name__ == "__main__":
    pass