from typing import List


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        N1 = len(A)
        N2 = len(B)
        if N1 != N2:
            return False
        if A == B:
            s = set(A)
            if len(s) < N1:
                return True
        res = []
        for i in range(N1):
            if A[i] != B[i]:
                res.append((A[i], B[i]))
            if len(res) > 2:
                return False
        if len(res) != 2:
            return False
        if res[0][0] == res[1][1] and res[0][1] == res[1][0]:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    result = s.buddyStrings("abcaa", "abcbb")
    print(result)
