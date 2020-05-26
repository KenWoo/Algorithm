from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        M = min([x[0] for x in ops])
        N = min([x[1] for x in ops])
        return M * N


if __name__ == "__main__":
    s = Solution()
    result = s.maxCount(3, 3, [[2, 2], [3, 3]])
    print(result)
