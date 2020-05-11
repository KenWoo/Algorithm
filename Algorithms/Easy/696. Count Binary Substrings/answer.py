from typing import List


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                res += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return res + min(prev, cur)


if __name__ == "__main__":
    s = Solution()
    result = s.countBinarySubstrings("00110011")
    print(result)
