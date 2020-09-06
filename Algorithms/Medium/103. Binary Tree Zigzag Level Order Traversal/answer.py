from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = []

        def preorder(node: TreeNode, level):
            if node:
                if len(self.res) < level + 1:
                    self.res.append([])
                if level % 2 == 0:
                    self.res[level].append(node.val)
                else:
                    self.res[level].insert(0, node.val)
                preorder(node.left, level+1)
                preorder(node.right, level+1)
        preorder(root, 0)
        return self.res


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    result = s.zigzagLevelOrder(root)
    print(result)
