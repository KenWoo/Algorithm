from typing import List


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        res = cur = j = 0
        for i in range(N):
            cur += abs(ord(s[i]) - ord(t[i]))
            while cur > maxCost:
                cur -= abs(ord(s[j]) - ord(t[j]))
                j += 1
            res = max(res, i - j + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.equalSubstring("krrgw", "zjxss", 19)
    print(result)
