from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        def subPathSub(node: TreeNode, sum: int) -> int:
            if not node:
                return 0
            res = 0
            if node.val == sum:
                res += 1
            res += subPathSub(node.left, sum-node.val)
            res += subPathSub(node.right, sum-node.val)
            return res

        return subPathSub(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


if __name__ == "__main__":
    s = Solution()
    node41 = TreeNode(3)
    node42 = TreeNode(-2)
    node43 = TreeNode(1)
    node31 = TreeNode(3)
    node31.left = node41
    node31.right = node42
    node32 = TreeNode(2)
    node32.right = node43
    node33 = TreeNode(11)
    node21 = TreeNode(5)
    node21.left = node31
    node21.right = node32
    node22 = TreeNode(-3)
    node22.right = node33
    root = TreeNode(10)
    root.left = node21
    root.right = node22
    result = s.pathSum(root, 8)
    print(result)
