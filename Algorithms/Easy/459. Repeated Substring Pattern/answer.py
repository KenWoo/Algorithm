from typing import List


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (2 * s)[1:-1]


if __name__ == "__main__":
    s = Solution()
    result = s.repeatedSubstringPattern("aba")
    print(result)
