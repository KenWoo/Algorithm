from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        N = len(arr)
        leftMax = [0] * N
        rightMin = [0] * N
        ma = float('-inf')
        for i in range(N):
            ma = max(ma, arr[i])
            leftMax[i] = ma
        mi = float('inf')
        for i in range(N-1, -1, -1):
            mi = min(mi, arr[i])
            rightMin[i] = mi
        res = 0
        for i in range(N-1):
            if leftMax[i] <= rightMin[i+1]:
                res += 1
        return res + 1


if __name__ == "__main__":
    s = Solution()
    result = s.maxChunksToSorted([2, 1, 3, 4, 4])
    print(result)
