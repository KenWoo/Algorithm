from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = m = sum(nums[:k])
        for i in range(k, len(nums)):
            m += nums[i] - nums[i-k]
            res = res if res > m else m
        return res / k


if __name__ == "__main__":
    s = Solution()
    result = s.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
    print(result)
