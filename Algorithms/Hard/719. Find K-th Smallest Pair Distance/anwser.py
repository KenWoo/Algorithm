from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def check(guess):
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = l + (r-l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == "__main__":
    s = Solution()
    result = s.smallestDistancePair([1, 3, 1], 1)
    print(result)
