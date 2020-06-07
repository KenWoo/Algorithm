from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        N = len(arr)
        m = arr[(N-1)//2]
        i, j = 0, N-1
        while N-(j-i) <= k:
            if abs(arr[i]-m) > abs(arr[j]-m):
                i += 1
            else:
                j -= 1
        return arr[:i] + arr[j+1:]


if __name__ == "__main__":
    s = Solution()
    result = s.getStrongest([1, 1, 3, 5, 5], 2)
    print(result)
