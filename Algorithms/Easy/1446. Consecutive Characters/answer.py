from typing import List


class Solution:
    def maxPower(self, s: str) -> int:
        i, N = 0, len(s)
        res = 0
        while i < N:
            j = i + 1
            while j < N and s[i] == s[j]:
                j += 1
            res = max(res, j - i)
            i = j
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maxPower("hooraaaaaaaaaaay")
    print(result)
