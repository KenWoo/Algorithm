from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def dfs(l, r):
            res = []
            if l > r:
                return [None]
            for i in range(l, r+1):
                l_t = dfs(l, i-1)
                r_t = dfs(i+1, r)
                for ll in l_t:
                    for rr in r_t:
                        root = TreeNode(i)
                        root.left = ll
                        root.right = rr
                        res.append(root)
            return res
        return dfs(1, n)
        
if __name__ == "__main__":
    pass