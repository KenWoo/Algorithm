from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in s:
            dict.setdefault(i, 0)
            dict[i] += 1
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    result = s.firstUniqChar("leetcode")
    print(result)
