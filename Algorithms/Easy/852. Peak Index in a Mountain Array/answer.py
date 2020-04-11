from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                l = mid
            elif A[mid] < A[mid-1] and A[mid] > A[mid+1]:
                r = mid
        return -1


if __name__ == "__main__":
    s = Solution()
    result = s.peakIndexInMountainArray([0, 1, 5, 4, 0])
    print(result)
