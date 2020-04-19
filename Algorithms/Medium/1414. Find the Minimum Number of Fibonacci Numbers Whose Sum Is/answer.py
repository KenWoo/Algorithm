from typing import List


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def constuctFib():
            fib = [1, 1]
            i = 2
            while True:
                next = fib[i-1] + fib[i-2]
                if next > k:
                    return fib
                fib.append(next)
                i += 1
        f = constuctFib()
        count, j = 0, len(f) - 1
        while k > 0:
            count += k // f[j]
            k = k % f[j]
            j -= 1
        return count


if __name__ == "__main__":
    s = Solution()
    result = s.findMinFibonacciNumbers(19)
    print(result)
