from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = []
        l.extend(nums1)
        l.extend(nums2)
        l.sort()
        N = len(l)
        return l[N // 2] if N % 2 != 0 else (l[N // 2 - 1] + l[N // 2]) / 2


if __name__ == "__main__":
    s = Solution()
    result = s.findMedianSortedArrays([1, 2], [3, 4])
    print(result)
