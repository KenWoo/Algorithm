from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            ll = dfs(node.left)
            rl = dfs(node.right)
            la = ra = 0
            if node.left and node.left.val == node.val:
                la = ll + 1
            if node.right and node.right.val == node.val:
                ra = rl + 1
            self.res = max(self.res, la + ra)
            return max(la, ra)
        dfs(root)
        return self.res


if __name__ == "__main__":
    pass
