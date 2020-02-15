from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0] * n
        isEven = n % 2 == 0
        if isEven:
            for i in range(n//2):
                res[i] = i+1
            for i in range(n//2, n):
                res[i] = -res[i-n//2]
        else:
            for i in range(n//2):
                res[i] = i+1
            for i in range(n//2+1, n):
                res[i] = -res[i-n//2-1]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.sumZero(11)
    print(result)
