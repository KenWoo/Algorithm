from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [None] * 2 * n
        for i in range(0, 2 * n, 2):
            res[i] = nums[i//2]
        for i in range(1, 2 * n, 2):
            res[i] = nums[n+i//2]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.shuffle([2, 5, 1, 3, 4, 7], 3)
    print(result)
