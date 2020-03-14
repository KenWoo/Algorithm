from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        N = len(arr)
        presum = [0] * (N+1)
        for i in range(1, N+1):
            presum[i] = presum[i-1] + arr[i-1]
        res = 0
        for i in range(1, N-k+2):
            s = presum[i+k-1] - presum[i-1]
            if s // k >= threshold:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5)
    print(result)
