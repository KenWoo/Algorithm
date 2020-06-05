from typing import List


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                si, sj = s[:i] + s[i+1:], s[:j] + s[j+1:]
                return si == si[::-1] or sj == sj[::-1]
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.validPalindrome("aba")
    print(result)
