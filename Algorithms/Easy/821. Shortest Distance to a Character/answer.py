from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        i, N = 0, len(S)
        l = []
        while i < N:
            if S[i] == C:
                l.append(i)
            i += 1
        d = [float('inf')] * N
        for i in l:
            for j in range(N):
                d[j] = min(d[j], abs(i-j))
        return d


if __name__ == "__main__":
    s = Solution()
    result = s.shortestToChar('loveleetcode', 'e')
    print(result)
