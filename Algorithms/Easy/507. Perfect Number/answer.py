from typing import List


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        sum = 0
        i = 1
        while i * i <= num:
            if num % i == 0:
                sum += i
                if i * i != num:
                    sum += num // i
            i += 1
        return sum - num == num


if __name__ == "__main__":
    s = Solution()
    result = s.checkPerfectNumber(28)
    print(result)
