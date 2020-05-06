from typing import List


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))


if __name__ == "__main__":
    s = Solution()
    result = s.findLUSlength("aba", "cdc")
    print(result)
