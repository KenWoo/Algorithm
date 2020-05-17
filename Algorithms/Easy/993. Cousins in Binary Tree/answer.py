from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.dict = {}

        def dfs(node, parent, depth):
            if not node:
                return
            self.dict[node.val] = (parent, depth)
            dfs(node.left, node, depth+1)
            dfs(node.right, node, depth+1)
        dfs(root, None, 0)
        px, dx = self.dict[x]
        py, dy = self.dict[y]
        return px != py and dx == dy


if __name__ == "__main__":
    pass
