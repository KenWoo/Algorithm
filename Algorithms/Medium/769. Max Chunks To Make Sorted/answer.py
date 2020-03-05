from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        m = res = 0
        for i in range(len(arr)):
            m = max(m, arr[i])
            if m == i:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maxChunksToSorted([1, 0, 2, 3, 4])
    print(result)
