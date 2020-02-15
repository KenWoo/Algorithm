from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            i = n // 10
            sum = 1
            while i != 0:
                i //= 10
                sum += 1
            if sum % 2 == 0:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findNumbers([555, 901, 482, 1771])
    print(result)
