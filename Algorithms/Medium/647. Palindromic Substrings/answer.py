from typing import List


class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0
        for center in range(2*N-1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.countSubstrings("aaa")
    print(result)
