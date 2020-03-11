from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N = len(customers)
        res = m = n = 0
        for i in range(N):
            if grumpy[i] == 0:
                res += customers[i]
            else:
                n += customers[i]
            if i + 1 > X:
                n -= customers[i-X] * grumpy[i-X]
            m = max(m, n)
        return res + m


if __name__ == "__main__":
    s = Solution()
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    result = s.maxSatisfied(customers, grumpy, X)
    print(result)
