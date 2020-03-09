from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def greedy(C):
            res = su = 0
            for w in weights:
                if su + w > C:
                    res += 1
                    su = 0
                su += w
            return res + bool(su)
        l, r = max(weights), sum(weights)
        while l <= r:
            mid = l + (r-l)//2
            t = greedy(mid)
            if t > D:
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == "__main__":
    s = Solution()
    result = s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    print(result)
