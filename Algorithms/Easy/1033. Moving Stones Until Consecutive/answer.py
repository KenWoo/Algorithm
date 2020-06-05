from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        maxer = c - a - 2
        miner = 1 if c - b == 2 or b - \
            a == 2 else min(c-b-1, 1) + min(b-a-1, 1)
        return [miner, maxer]


if __name__ == "__main__":
    s = Solution()
    result = s.numMovesStones(1, 2, 5)
    print(result)
