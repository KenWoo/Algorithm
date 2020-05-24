from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        dict = {}
        N = len(nums)
        for i in range(N):
            dict[nums[i]] = i
        l = sorted(dict.items(), key=lambda x: x[0], reverse=True)
        for i in range(N):
            item = l[i]
            index = item[1]
            if i == 0:
                nums[index] = 'Gold Medal'
            elif i == 1:
                nums[index] = 'Silver Medal'
            elif i == 2:
                nums[index] = 'Bronze Medal'
            else:
                nums[index] = str(i + 1)
        return nums


if __name__ == "__main__":
    s = Solution()
    result = s.findRelativeRanks([1, 4, 3, 2, 5])
    print(result)
