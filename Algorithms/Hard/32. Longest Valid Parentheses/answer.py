from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        N = len(s)
        dp = [0] * N
        for i in range(1, N):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (0 if i < 2 else dp[i-2]) + 2 
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + (0 if i-dp[i-1] < 2 else dp[i-dp[i-1]-2]) + 2
                res = max(res, dp[i])
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.longestValidParentheses("()(())")
    print(result)