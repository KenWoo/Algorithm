from typing import List


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        pal = True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                pal = False
                break
            l += 1
            r -= 1
        return 1 if pal else 2


if __name__ == "__main__":
    s = Solution()
    result = s.removePalindromeSub("ababa")
    print(result)
