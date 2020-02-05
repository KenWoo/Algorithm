from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        m = len(bits)
        while i < m - 1:
            i += bits[i] + 1
        return i == m - 1


if __name__ == "__main__":
    s = Solution()
    result = s.isOneBitCharacter([1, 1, 1, 0])
    print(result)
