from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        N = len(nums)
        target = [None] * N
        for i in range(N):
            idx = index[i]
            if target[idx] is None:
                target[idx] = nums[i]
            else:
                for j in range(N-2, idx-1, -1):
                    target[j+1] = target[j]
                target[idx] = nums[i]
        return target


if __name__ == "__main__":
    s = Solution()
    result = s.createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0])
    print(result)
