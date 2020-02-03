from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums

        l = [c for r in nums for c in r]
        matrix = []
        for i in range(0, len(l), c):
            matrix.append(l[i: i + c])
        return matrix


if __name__ == "__main__":
    s = Solution()
    result = s.matrixReshape([[1, 2], [3, 4]], 4, 1)
    print(result)
