from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        j = N - 1
        while j > 0 and arr[j-1] <= arr[j]:
            j -= 1
        if j == 0:
            return 0
        res = j
        for i in range(N):
            if i > 0 and arr[i-1] > arr[i]:
                break
            while j < N and arr[i] > arr[j]:
                j += 1
            res = min(res, j - i - 1)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5])
    print(result)
