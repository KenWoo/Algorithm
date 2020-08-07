from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inOrder(root):
            if not root: return
            inOrder(root.left)
            if self.pre and self.pre.val > root.val:
                if not self.first:
                    self.first = self.pre
                self.second = root
            self.pre = root
            inOrder(root.right) 

        self.pre, self.first, self.second = None, None, None
        inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val                   

if __name__ == "__main__":
    pass