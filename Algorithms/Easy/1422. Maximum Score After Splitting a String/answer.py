from typing import List


class Solution:
    def maxScore(self, s: str) -> int:
        l, r = s[0], s[1:]
        zero = 1 if l == '0' else 0
        one = 0
        for i in range(len(r)):
            if r[i] == '1':
                one += 1
        res = zero + one
        for i in range(len(r)-1):
            if r[i] == '0':
                zero += 1
            else:
                one -= 1
            res = max(res, zero+one)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maxScore("00")
    print(result)
