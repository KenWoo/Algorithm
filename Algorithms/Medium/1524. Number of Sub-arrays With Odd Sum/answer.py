from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res, odd, even = 0, 0, 0
        for x in arr:
            if x & 1:
                odd, even = even + 1, odd
            else:
                odd, even = odd, even + 1
            res += odd
        return res % int(1e9 + 7)


if __name__ == "__main__":
    s = Solution()
    result = s.numOfSubarrays([1, 3, 5])
    print(result)
