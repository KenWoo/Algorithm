from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 1, None, None, 0
            fl, minl, maxl, retl = dfs(node.left)
            fr, minr, maxr, retr = dfs(node.right)
            if fl and fr and (maxl is None or maxl < node.val) and (minr is None or minr > node.val):
                ret = node.val + retl + retr
                self.res = max(self.res, ret)
                return 1, node.val if minl is None else minl, node.val if maxr is None else maxr, ret
            return 0, None, None, 0
        dfs(root)
        return self.res

if __name__ == "__main__":
    pass