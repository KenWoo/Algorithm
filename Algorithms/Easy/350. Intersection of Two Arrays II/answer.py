from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        for n in nums1:
            dict1.setdefault(n, 0)
            dict1[n] += 1
        dict2 = {}
        for n in nums2:
            dict2.setdefault(n, 0)
            dict2[n] += 1
        res = []
        for k, v in dict1.items():
            if k in dict2:
                n = min(v, dict2[k])
                for _ in range(n):
                    res.append(k)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.intersect([1, 2, 2, 1], [2, 2])
    print(result)
