from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        f, s = head, head.next
        while f and s:
            f.val, s.val = s.val, f.val
            if not f.next or not s.next:
                break
            f = f.next.next
            s = s.next.next
        return head


if __name__ == "__main__":
    pass