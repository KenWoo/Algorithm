from typing import List


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 != 0:
            return ''.join(['a'] * n)
        else:
            return ''.join(['a'] * (n-1) + ['b'])


if __name__ == "__main__":
    s = Solution()
    result = s.generateTheString(4)
    print(result)
