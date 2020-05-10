from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        pre = [0] * (N+1)
        for i in range(1, N+1):
            pre[i] = pre[i-1] ^ arr[i-1]
        res = 0
        for i in range(N+1):
            for j in range(i+2, N+1):
                if pre[i] == pre[j]:
                    res += j-i-1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.countTriplets([2, 3, 1, 6, 7])
    print(result)
