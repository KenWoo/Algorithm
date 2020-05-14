from typing import List


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        N, M = len(str1), len(str2)
        if N == 0:
            return str2
        for i in range(N):
            if str1[i] != str2[i]:
                return ""
        return self.gcdOfStrings(str1, str2[N:M])


if __name__ == "__main__":
    s = Solution()
    result = s.gcdOfStrings("ABABAB", "ABAB")
    print(result)
