from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N-1):
            for j in range(i+1, N):
                if nums[i] == nums[j]:
                    res += 1
        return res
        

if __name__ == "__main__":
    s = Solution()
    result = s.numIdenticalPairs([1,1,1,1])
    print(result)