from typing import List


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        for i in range(1, N + 1):
            if i == 1:
                a, b = 0, 1
            else:
                a, b = b, a + b
        return b


if __name__ == "__main__":
    s = Solution()
    result = s.fib(3)
    print(result)
