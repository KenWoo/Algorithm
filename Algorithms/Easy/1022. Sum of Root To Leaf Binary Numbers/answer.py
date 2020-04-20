from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        def dps(node, total):
            if not node:
                return 0
            total += node.val
            if not node.left and not node.right:
                return total
            return dps(node.left, total*2) + dps(node.right, total*2)
        return dps(root, 0)


if __name__ == "__main__":
    pass
