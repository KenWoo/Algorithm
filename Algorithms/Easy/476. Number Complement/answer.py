from typing import List


class Solution:
    def findComplement(self, num: int) -> int:
        N = len(bin(num)[2:])
        c = "1" * N
        b = num ^ int(c, 2)
        return b


if __name__ == "__main__":
    s = Solution()
    result = s.findComplement(5)
    print(result)
