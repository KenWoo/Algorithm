from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for i in s:
            p = t.find(i, start)
            if p == -1:
                return False
            start = p + 1
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.isSubsequence("axc", "ahbgdc")
    print(result)
