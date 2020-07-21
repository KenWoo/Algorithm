from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.
        if n == 0:
            return res
        x = x if n > 0 else 1 / x
        n = abs(n)
        res = x ** n
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.myPow(2.00000, -2)
    print(result)