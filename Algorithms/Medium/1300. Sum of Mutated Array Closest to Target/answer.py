from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()

        def sum(m):
            res = 0
            for i in range(len(arr)):
                if arr[i] > m:
                    res += m
                else:
                    res += arr[i]
            return res
        l, r = 0, target
        while l <= r:
            mid = l + (r-l)//2
            s = sum(mid)
            if s == target:
                return mid
            elif s > target:
                r = mid - 1
            else:
                l = mid + 1
        return l if abs(sum(l)-target) < abs(sum(l-1)-target) else l-1


if __name__ == "__main__":
    s = Solution()
    result = s.findBestValue([2, 3, 5], 10)
    print(result)
