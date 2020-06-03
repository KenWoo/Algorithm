from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.res = float('inf')
        min = root.val

        def dfs(node):
            if node:
                if min < node.val < self.res:
                    self.res = node.val
                elif node.val == min:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.res if self.res < float('inf') else -1


if __name__ == "__main__":
    pass
