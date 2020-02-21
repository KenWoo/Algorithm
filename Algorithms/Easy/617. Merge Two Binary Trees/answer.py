from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


if __name__ == "__main__":
    s = Solution()
    t1node21 = TreeNode(5)
    t1node11 = TreeNode(3)
    t1node11.left = t1node21
    t1node12 = TreeNode(2)
    t1root = TreeNode(1)
    t1root.left = t1node11
    t1root.right = t1node12
    t2node22 = TreeNode(4)
    t2node23 = TreeNode(7)
    t2node11 = TreeNode(1)
    t2node11.right = t2node22
    t2node12 = TreeNode(3)
    t2node12.right = t2node12
    t2root = TreeNode(2)
    t2root.left = t2node11
    t2root.right = t2node12
    result = s.mergeTrees(t1root, t2root)
    print(result)
