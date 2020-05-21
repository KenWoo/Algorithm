from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0

        def dfs(node, isLeft):
            if not node:
                return
            if isLeft and not node.left and not node.right:
                self.sum += node.val
            dfs(node.left, True)
            dfs(node.right, False)
        dfs(root, False)
        return self.sum


if __name__ == "__main__":
    pass
