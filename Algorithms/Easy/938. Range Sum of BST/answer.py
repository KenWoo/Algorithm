from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res, stack = 0, [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val >= L and node.val <= R:
                    res += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return res


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    result = s.rangeSumBST(root, 5, 15)
    print(result)
