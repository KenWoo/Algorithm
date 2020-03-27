from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        N = len(l)
        res = 0
        for i, v in enumerate(l):
            if v == 1:
                res += 2 ** (N-i-1)
        return res


if __name__ == "__main__":
    s = Solution()
    root = ListNode(1)
    next = ListNode(0)
    last = ListNode(1)
    root.next = next
    next.next = last
    result = s.getDecimalValue(root)
    print(result)
