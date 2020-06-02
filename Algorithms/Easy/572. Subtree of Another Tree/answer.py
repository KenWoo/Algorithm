from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def preorder(n, left):
            if not n:
                if left:
                    return 'lnull'
                else:
                    return 'rnull'
            return '#' + str(n.val) + preorder(n.left, True) + preorder(n.right, False)
        tree1 = preorder(s, True)
        tree2 = preorder(t, True)
        return tree1.find(tree2) >= 0


if __name__ == "__main__":
    pass
