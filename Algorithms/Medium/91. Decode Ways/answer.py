from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(2, len(s)+1):
            if 10 <= int(s[i-2:i]) <= 26 and s[i-1] != '0':
                dp.append(dp[i-1] + dp[i-2])
            elif int(s[i-2:i]) in [10, 20]:
                dp.append(dp[i-2])
            elif s[i-1] != '0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]

if __name__ == "__main__":
    s = Solution()
    result = s.numDecodings('12')
    print(result)