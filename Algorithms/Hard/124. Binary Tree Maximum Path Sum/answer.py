from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = root.val
        def dfs(node):
            if not node:
                return 0
            s, l, r = node.val, 0, 0     
            if node.left:
                l = dfs(node.left)       
                if l > 0:
                    s += l
            if node.right:
                r = dfs(node.right)
                if r > 0:
                    s += r
            self.res = max(self.res, s)
            return max(node.val, max(node.val+l, node.val+r))
        dfs(root)
        return self.res

if __name__ == "__main__":
    pass