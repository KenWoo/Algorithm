from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0

        def dfs(node):
            if node:
                dfs(node.right)
                self.total += node.val
                node.val = self.total
                dfs(node.left)
            return node
        return dfs(root)


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5)
    result = s.convertBST(root)
    print(result.val)
