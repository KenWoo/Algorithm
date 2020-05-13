from typing import List


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = [0] * 26
        for c in s:
            ss[ord(c)-ord('a')] += 1
        tt = [0] * 26
        for c in t:
            tt[ord(c)-ord('a')] += 1
        for i in range(26):
            if ss[i] != tt[i]:
                return chr(i + ord('a'))


if __name__ == "__main__":
    s = Solution()
    result = s.findTheDifference("abcd", "abcde")
    print(result)
