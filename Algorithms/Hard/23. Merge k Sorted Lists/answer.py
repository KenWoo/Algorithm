from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        head = node = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for n in sorted(nodes):
            node.next = ListNode(n)
            node = node.next
        return head.next

if __name__ == "__main__":
    pass