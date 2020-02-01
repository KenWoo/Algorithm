from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        s = set(nums)
        for i in range(len(nums)):
            if i + 1 not in s:
                result.append(i + 1)
        return result


if __name__ == "__main__":
    s = Solution()
    result = s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print(result)
