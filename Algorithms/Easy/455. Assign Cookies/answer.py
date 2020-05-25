from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = res = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
            j += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findContentChildren([1, 2, 3], [1, 1])
    print(result)
