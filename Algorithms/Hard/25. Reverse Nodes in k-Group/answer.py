from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pre = ListNode(-1)
        tail = pre
        q = head
        while q is not None:
            n = k
            p = q
            while p is not None and n > 0:
                p = p.next
                n -= 1
            if n > 0:
                tail.next = q
                break
            end = q
            while q != p:
                t = q.next
                q.next = tail.next
                tail.next = q
                q = t
            tail = end
        return pre.next        

if __name__ == "__main__":
    pass