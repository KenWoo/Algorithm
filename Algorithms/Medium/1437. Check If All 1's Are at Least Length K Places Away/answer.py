from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        indexes = []
        for i in range(len(nums)):
            if nums[i] == 1:
                indexes.append(i)
        for i in range(len(indexes)-1):
            if indexes[i+1] - indexes[i] - 1 < k:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.kLengthApart([0, 1, 0, 1], 2)
    print(result)
