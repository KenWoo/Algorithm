from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res = float('inf')
        self.pre = -1

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.pre != -1:
                self.res = min(self.res, node.val - self.pre)
            self.pre = node.val
            inorder(node.right)
        inorder(root)
        return self.res


if __name__ == "__main__":
    pass
