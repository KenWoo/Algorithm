from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dps(node, vlist):
            if not node:
                return
            if not node.left and not node.right:
                vlist.append(node.val)
            dps(node.left, vlist)
            dps(node.right, vlist)
        l1 = []
        l2 = []
        dps(root1, l1)
        dps(root2, l2)
        return l1 == l2


if __name__ == "__main__":
    pass
