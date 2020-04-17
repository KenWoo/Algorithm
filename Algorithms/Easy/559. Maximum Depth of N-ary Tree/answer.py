from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        dep = 0
        for c in root.children:
            dep = max(dep, self.maxDepth(c))
        return dep + 1


if __name__ == "__main__":
    s = Solution()
    children = [Node(3, []), Node(2, []), Node(4, [])]
    root = Node(1, children)
    result = s.maxDepth(root)
    print(result)
