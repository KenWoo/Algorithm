from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        stack = []
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
        res = [root.val]
        while stack:
            s = c = 0
            tmp = []
            while stack:
                node = stack.pop()
                if node:
                    s += node.val
                    c += 1
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
            res.append(s / c)
            stack = tmp
        return res


if __name__ == "__main__":
    pass
