from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = miss = -1
        N = len(nums)
        arr = [0] * (N + 1)
        for n in nums:
            arr[n] += 1
        for i in range(1, N+1):
            if arr[i] > 1:
                dup = i
            elif arr[i] == 0:
                miss = i
        return [dup, miss]


if __name__ == "__main__":
    s = Solution()
    result = s.findErrorNums([1, 2, 2, 4])
    print(result)
