from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        start = 0
        end = len(height) - 1
        while start < end:
            res = max(res, (end-start)*min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)
