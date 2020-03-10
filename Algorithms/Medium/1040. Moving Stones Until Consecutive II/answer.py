from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        N = len(stones)
        high = max(stones[-1]-stones[1]-(N-2), stones[-2]-stones[0]-(N-2))
        low = N
        i = 0
        for j in range(N):
            while stones[j]-stones[i] >= N:
                i += 1
            if j-i+1 == N-1 and stones[j]-stones[i] == N-2:
                low = min(low, 2)
            else:
                low = min(low, N-(j-i+1))
        return [low, high]


if __name__ == "__main__":
    s = Solution()
    result = s.numMovesStonesII([7, 4, 9])
    print(result)
