from typing import List


class Solution:
    def longestDecomposition(self, text: str) -> int:
        memo = {}

        def helper(s):
            n = len(s)
            if n <= 1:
                return n
            if s in memo:
                return memo[s]
            res = 1
            for i in range(n//2):
                if s[:i+1] == s[-i-1:]:
                    res = max(res, 2+helper(s[i+1:len(s)-i-1]))
            memo[s] = res
            return res

        res = helper(text)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi")
    print(result)
