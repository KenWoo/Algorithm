from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.count = 0
        self.current = 0
        self.maxCount = 0
        self.res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.count += 1
            if node.val != self.current:
                self.current = node.val
                self.count = 1
            if self.count > self.maxCount:
                self.maxCount = self.count
                self.res.clear()
                self.res.append(node.val)
            elif self.count == self.maxCount:
                self.res.append(node.val)
            inorder(node.right)
        inorder(root)
        return self.res


if __name__ == "__main__":
    pass
