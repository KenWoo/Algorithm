from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        level = res = 0
        while l < r:
            if height[l] < height[r]:
                idx = l
                l += 1
            else:
                idx = r
                r -= 1
            lower = height[idx]
            level = max(level, lower)
            res += level - lower
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(result)
