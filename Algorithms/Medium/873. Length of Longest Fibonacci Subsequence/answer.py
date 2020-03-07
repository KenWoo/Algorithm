from typing import List
import collections


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        indexes = {x: i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda: 2)

        res = 0
        for k in range(len(A)):
            for j in range(k):
                i = indexes.get(A[k]-A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    res = max(res, cand)
        return res if res >= 3 else 0


if __name__ == "__main__":
    s = Solution()
    result = s.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8])
    print(result)
