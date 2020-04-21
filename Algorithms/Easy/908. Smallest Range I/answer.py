from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A)-min(A) - 2*K)


if __name__ == "__main__":
    s = Solution()
    result = s.smallestRangeI([0, 10], 2)
    print(result)
