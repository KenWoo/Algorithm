from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        res = []
        N = len(A)
        S = str(K)
        M = len(S)
        i = N - 1
        j = M - 1
        carry = 0
        while i >= 0 or j >= 0 or carry != 0:
            v = carry
            if i >= 0:
                v += A[i]
            if j >= 0:
                v += int(S[j])
            carry, rem = divmod(v, 10)
            res.append(rem)
            i -= 1
            j -= 1
        return list(reversed(res))


if __name__ == "__main__":
    s = Solution()
    result = s.addToArrayForm([2, 1, 5], 806)
    print(result)
