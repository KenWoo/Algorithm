from typing import List


class Solution:
    def reformat(self, s: str) -> str:
        N = []
        S = []
        for c in s:
            if c.isnumeric():
                N.append(c)
            else:
                S.append(c)
        if abs(len(N) - len(S)) > 1:
            return ""
        res = []
        flag = len(N) >= len(S)
        for _ in range(len(s)):
            if flag:
                res.append(N.pop())
            else:
                res.append(S.pop())
            flag = not flag
        return ''.join(res)


if __name__ == "__main__":
    s = Solution()
    result = s.reformat("covid2019")
    print(result)
