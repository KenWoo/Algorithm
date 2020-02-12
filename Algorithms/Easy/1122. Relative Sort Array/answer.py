from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict = {}
        for n in arr1:
            dict.setdefault(n, 0)
            dict[n] += 1

        l = []
        for n in arr2:
            if n in dict:
                l.extend([n] * dict[n])
                dict.pop(n)
        for k in sorted(dict.keys()):
            l.extend([k] * dict[k])
        return l


if __name__ == "__main__":
    s = Solution()
    result = s.relativeSortArray(
        [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31], [2, 42, 38, 0, 43, 21])
    print(result)
