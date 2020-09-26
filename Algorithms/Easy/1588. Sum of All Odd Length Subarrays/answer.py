from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        N = len(arr)
        for i in range(1, N+1, 2):
            for j in range(N-i+1):
                res += sum(arr[j:j+i])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.sumOddLengthSubarrays([1])
    print(result)
