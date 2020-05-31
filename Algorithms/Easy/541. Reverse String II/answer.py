from typing import List


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        i = 0
        N = len(s)
        while i < N:
            c = 0
            while i+c < N and c < k:
                c += 1
            res += ''.join(reversed(s[i:c+i]))
            i += c
            while i+c < N and c < k:
                c += 1
            res += s[i:c+i]
            i += c
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.reverseStr("abcdefs234g", 2)
    print(result)
