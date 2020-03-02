from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N, sum, res = len(nums), 0, 0
        dict = {}
        dict[0] = 1
        for i in range(N):
            sum += nums[i]
            if sum-k in dict:
                res += dict[sum-k]
            dict.setdefault(sum, 0)
            dict[sum] += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.subarraySum([1, 1, 1, 1], 3)
    print(result)
