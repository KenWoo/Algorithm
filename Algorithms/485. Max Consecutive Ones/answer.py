from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = count = 0
        for n in nums:
            if n == 1:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0

        return max_count


if __name__ == "__main__":
    s = Solution()
    result = s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
    print(result)
