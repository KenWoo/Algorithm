from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        N, res = len(nums), 0
        for i in range(N):
            if nums[i] != float('inf'):
                start, count = nums[i], 0
                while nums[start] != float('inf'):
                    temp = start
                    start = nums[start]
                    nums[temp] = float('inf')
                    count += 1
                res = max(res, count)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.arrayNesting([5, 4, 0, 3, 1, 6, 2])
    print(result)
