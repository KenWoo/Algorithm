from typing import List
import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def countPrime(n):
            count = 0
            for i in range(2, n+1):
                flag = True
                for j in range(2, int(math.sqrt(i))+1):
                    if i % j == 0:
                        flag = False
                        break
                if flag:
                    count += 1
            return count
        prime = countPrime(n)
        noprime = n - prime
        res, mod = 1, 10 ** 9 + 7
        for i in range(2, prime+1):
            res = (res * i) % mod
        for i in range(2, noprime+1):
            res = (res * i) % mod
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.numPrimeArrangements(5)
    print(result)
