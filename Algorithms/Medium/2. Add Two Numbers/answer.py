from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = node = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, rem = divmod(v1+v2+carry, 10)
            node.next = ListNode(rem)
            node = node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return h.next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(6)

    result = s.addTwoNumbers(l1, l2)
    while result is not None:
        print(result.val)
        result = result.next
