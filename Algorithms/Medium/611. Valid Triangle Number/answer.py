from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        res = 0
        for i in range(N-2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i+1, N-1):
                while k < N and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += k - j - 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.triangleNumber([0, 1, 0, 1])
    print(result)
