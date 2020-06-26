from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(l1, l2):
            h = ListNode(0)
            m = h
            if not l1:
                return l2
            if not l2:
                return l1
            while l1 and l2:
                if l1.val < l2.val:
                    m.next = l1
                    l1 = l1.next
                else:
                    m.next = l2
                    l2 = l2.next
                m = m.next
            m.next = l1 if l1 else l2
            return h.next
        if not head or not head.next:
            return head
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        f = self.sortList(head)
        s = self.sortList(slow)
        return merge(f, s)


if __name__ == "__main__":
    pass
