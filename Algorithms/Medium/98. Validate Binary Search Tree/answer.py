from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not dfs(node.right, val, upper):
                return False
            if not dfs(node.left, lower, val):
                return False
            return True
        return dfs(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    pass
