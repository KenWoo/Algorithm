from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None

        last = postorder[-1]
        root = TreeNode(last)
        index = inorder.index(last)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root


if __name__ == "__main__":
    s = Solution()
    result = s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(result)
