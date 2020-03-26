from typing import List


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = r = 0
        res = 0
        for n in s:
            if n == 'L':
                l += 1
            else:
                r += 1
            if l == r:
                res += 1
                l = r = 0
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.balancedStringSplit("RLRRLLRLRL")
    print(result)
