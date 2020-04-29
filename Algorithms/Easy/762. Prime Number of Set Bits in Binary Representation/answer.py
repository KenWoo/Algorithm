from typing import List


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def isPrime(n):
            if n == 1:
                return False
            for i in range(2, n//2+1):
                if n % i == 0:
                    return False
            else:
                return True
        res = 0
        for i in range(L, R+1):
            c = int(bin(i).count('1'))
            if isPrime(c):
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.countPrimeSetBits(10, 15)
    print(result)
