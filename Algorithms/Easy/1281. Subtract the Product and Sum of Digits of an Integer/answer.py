from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = []
        while n > 0:
            rem = n % 10
            n = n // 10
            nums.append(rem)
        s = sum(nums)
        p = 1
        for i in nums:
            p *= i
        return p - s


if __name__ == "__main__":
    s = Solution()
    result = s.subtractProductAndSum(4421)
    print(result)
