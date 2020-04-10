from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for a in arr:
            dict.setdefault(a, 0)
            dict[a] += 1
        v = dict.values()
        N = len(v)
        M = len(set(v))
        return N == M


if __name__ == "__main__":
    s = Solution()
    result = s.uniqueOccurrences([1, 2])
    print(result)
