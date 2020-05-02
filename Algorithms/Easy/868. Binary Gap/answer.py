from typing import List


class Solution:
    def binaryGap(self, N: int) -> int:
        s = bin(N)
        l = s.find('1')
        res = 0
        while l != -1:
            r = s.find('1', l+1)
            if r != -1:
                res = max(res, r - l)
                l = s.find('1', r)
            else:
                break
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.binaryGap(22)
    print(result)
