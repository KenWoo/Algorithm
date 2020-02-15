from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i, row in enumerate(mat):
            res.append((sum([s for s in row if s == 1]), i))
        res.sort(key=lambda c: (c[0], c[1]))
        return [r[1] for r in res][:k]


if __name__ == "__main__":
    s = Solution()
    result = s.kWeakestRows([[1, 0, 0, 0],
                             [1, 1, 1, 1],
                             [1, 0, 0, 0],
                             [1, 0, 0, 0]], 4)
    print(result)
