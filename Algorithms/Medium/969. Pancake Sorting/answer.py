from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        sortedA = sorted(A)
        N = len(A)
        n = N - 1
        res = []
        for i in range(N-1, 0, -1):
            idx = A.index(sortedA[i])
            j = 0
            while j <= idx//2:
                A[j], A[idx-j] = A[idx-j], A[j]
                j += 1
            res.append(idx+1)
            k = 0
            while k <= n//2:
                A[k], A[n-k] = A[n-k], A[k]
                k += 1
            res.append(n+1)
            n -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.pancakeSort([3, 2, 4, 1])
    print(result)
