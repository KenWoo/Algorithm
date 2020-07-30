from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = ListNode(next=head)
        pre = tmp
        cur=pre.next
        while cur:
            while cur.next and cur.next.val==pre.next.val:
                cur=cur.next
            if pre.next==cur:
                pre=pre.next
            else:
                pre.next=cur.next
            cur=cur.next
        return tmp.next
        
if __name__ == "__main__":
    pass