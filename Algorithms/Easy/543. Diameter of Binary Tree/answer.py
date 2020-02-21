from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0

        def depth(node: TreeNode) -> int:
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        depth(root)
        return self.res


if __name__ == "__main__":
    s = Solution()
    node21 = TreeNode(4)
    node22 = TreeNode(5)
    node11 = TreeNode(2)
    node11.left = node21
    node11.right = node22
    node12 = TreeNode(3)
    root = TreeNode(1)
    root.left = node11
    root.right = node12
    result = s.diameterOfBinaryTree(root)
    print(result)
