from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for n in range(left, right+1):
            x, y = n, 0
            is_valid = True
            while x > 0:
                y = x % 10
                x //= 10
                if y == 0 or n % y != 0:
                    is_valid = False
                    break
            if is_valid:
                res.append(n)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.selfDividingNumbers(1, 22)
    print(result)
