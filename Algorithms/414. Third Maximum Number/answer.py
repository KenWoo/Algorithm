from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_1 = nums[0]
        max_2 = max_3 = None
        for i in range(1, len(nums)):
            item = nums[i]
            if max_2 is None and item < max_1:
                max_2 = item
            elif max_3 is None and max_2 is not None and item < max_2:
                max_3 = item

            if item > max_1:
                max_1, max_2, max_3 = item, max_1, max_2
            elif max_2 is not None and item > max_2 and item < max_1:
                max_2, max_3 = item, max_2
            elif max_2 is not None and max_3 is not None and item > max_3 and item < max_2:
                max_3 = item

        return max_3 if max_3 is not None else max_1


if __name__ == "__main__":
    s = Solution()
    result = s.thirdMax([1, 2, 2])
    print(result)
