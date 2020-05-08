from typing import List


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n in [1, 2]:
            return 1
        else:
            res = [0, 1, 1]
            for _ in range(3, n+1):
                res.append(res[-1] + res[-2] + res[-3])
            return res[-1]


if __name__ == "__main__":
    s = Solution()
    result = s.tribonacci(25)
    print(result)
