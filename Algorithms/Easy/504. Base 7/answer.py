from typing import List


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        n = abs(num)
        res = ''
        while n:
            res = str(n % 7) + res
            n //= 7
        return res if num >= 0 else '-' + res


if __name__ == "__main__":
    s = Solution()
    result = s.convertToBase7(100)
    print(result)
