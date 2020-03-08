from typing import List


class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        N = len(S)
        P = [0]
        for s in S:
            P.append(P[-1] + int(s))
        return min([P[i] + (N-P[-1]) - (i-P[i]) for i in range(len(P))])


if __name__ == "__main__":
    s = Solution()
    result = s.minFlipsMonoIncr("0101100011")
    print(result)
