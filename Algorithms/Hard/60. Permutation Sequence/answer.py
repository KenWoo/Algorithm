from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ''
        fact = [1] * n
        num = [str(i) for i in range(1, 10)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        k -= 1
        for i in range(n, 0, -1):
            first = k // fact[i - 1]
            k %= fact[i - 1]
            res += num[first]
            num.pop(first)
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.getPermutation(3, 3)
    print(result)