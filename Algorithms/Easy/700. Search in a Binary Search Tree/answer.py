from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


if __name__ == "__main__":
    pass