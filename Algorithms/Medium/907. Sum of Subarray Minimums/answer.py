from typing import List


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        res = dot = 0
        for i, val in enumerate(A):
            count = 1
            while stack and stack[-1][0] >= val:
                v, c = stack.pop()
                count += c
                dot -= v*c
            stack.append((val, count))
            dot += val*count
            res += dot
        return res % MOD


if __name__ == "__main__":
    s = Solution()
    result = s.sumSubarrayMins([3, 1, 2, 4])
    print(result)
