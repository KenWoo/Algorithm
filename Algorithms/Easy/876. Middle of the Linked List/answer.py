from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        nodes = [head]
        while nodes[-1].next:
            nodes.append(nodes[-1].next)
        return nodes[len(nodes) // 2]


if __name__ == "__main__":
    pass
