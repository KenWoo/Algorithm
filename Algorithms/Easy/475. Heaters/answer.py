from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        j = 0
        for i in range(len(houses)):
            cur = houses[i]
            while j < len(heaters) - 1 and abs(heaters[j+1]-cur) <= abs(heaters[j]-cur):
                j += 1
            res = max(res, abs(heaters[j]-cur))
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findRadius([1, 2, 3], [2])
    print(result)
