from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return set(target) == set(arr)


if __name__ == "__main__":
    s = Solution()
    result = s.canBeEqual([1, 2, 3, 4], [2, 4, 1, 3])
    print(result)
