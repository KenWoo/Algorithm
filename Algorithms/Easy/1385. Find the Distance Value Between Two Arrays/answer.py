from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for a in arr1:
            flag = True
            for b in arr2:
                if abs(a-b) <= d:
                    flag = False
                    break
            if flag:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findTheDistanceValue(
        [1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3)
    print(result)
