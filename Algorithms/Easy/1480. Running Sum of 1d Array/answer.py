from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = nums[0]
        for i in range(1, len(nums)):
            nums[i] += s
            s = nums[i]
        return nums

if __name__ == "__main__":
    s = Solution()
    result = s.runningSum([3,1,2,10,1])
    print(result)