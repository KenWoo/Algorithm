from typing import List


class Solution:
    def countLargestGroup(self, n: int) -> int:
        dict = {}
        for i in range(1, n+1):
            x, y = i, 0
            while x > 0:
                y += x % 10
                x //= 10
            dict.setdefault(y, 0)
            dict[y] += 1
        ma = 0
        for v in dict.values():
            ma = max(ma, v)
        res = 0
        for v in dict.values():
            if v == ma:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.countLargestGroup(15)
    print(result)
