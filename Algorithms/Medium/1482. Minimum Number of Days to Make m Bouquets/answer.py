from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def check(x):
            count = step = 0
            for d in bloomDay:
                if x >= d:
                    step += 1
                else:
                    step = 0
                if step == k:
                    count += 1
                    step = 0
            return count >= m
        l, r = min(bloomDay), max(bloomDay)+1
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        if l > max(bloomDay):
            return -1
        return l


if __name__ == "__main__":
    s = Solution()
    result = s.minDays([1, 10, 3, 10, 2], 3, 1)
    print(result)
