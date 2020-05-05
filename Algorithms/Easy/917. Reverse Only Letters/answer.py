from typing import List


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        l, r = 0, len(s)-1
        while l < r:
            while not s[l].isalpha() and l < r:
                l += 1
            while not s[r].isalpha() and l < r:
                r -= 1
            if l >= r:
                break
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


if __name__ == "__main__":
    s = Solution()
    result = s.reverseOnlyLetters("Test1ng-Leet=code-Q!")
    print(result)
