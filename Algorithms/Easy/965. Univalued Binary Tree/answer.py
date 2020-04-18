from typing import List


def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = []
        v = -1
        if root:
            stack.append(root)
            v = root.val
        while stack:
            node = stack.pop()
            if v != node.val:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True


if __name__ == "__main__":
    pass
