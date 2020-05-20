from typing import List
from heapq import *


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapify(A)
        for _ in range(K):
            x = heappop(A)
            x = -x
            heappush(A, x)
        return sum(A)


if __name__ == "__main__":
    s = Solution()
    result = s.largestSumAfterKNegations([4, 2, 3], 1)
    print(result)
