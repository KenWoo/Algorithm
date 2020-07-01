from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        f, s = head, head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
            if s == f:
                while f != head:
                    f = f.next
                    head = head.next
                return head
        return None
        

if __name__ == "__main__":
    pass