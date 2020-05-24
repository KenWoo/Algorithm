from typing import List


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A+A


if __name__ == "__main__":
    s = Solution()
    result = s.rotateString('abcde', 'cdeab')
    print(result)
