from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N1 = len(nums1)
        N2 = len(nums2)
        res = [-1] * N1
        for i in range(N1):
            n1 = nums1[i]
            idx = nums2.index(n1)
            while idx < N2:
                if nums2[idx] > n1:
                    res[i] = nums2[idx]
                    break
                idx += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.nextGreaterElement([2, 4], [1, 2, 3, 4])
    print(result)
