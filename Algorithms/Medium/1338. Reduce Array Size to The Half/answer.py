from typing import List
import collections


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dict = collections.Counter(arr)
        sorted_value = sorted(dict.values(), reverse=True)
        N = len(arr)
        res = count = 0
        for i in range(len(sorted_value)):
            count += sorted_value[i]
            if count >= N//2:
                res = i+1
                break
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7])
    print(result)
    result = s.minSetSize([7, 7, 7, 7, 7, 7])
    print(result)
    result = s.minSetSize([1, 9])
    print(result)
    result = s.minSetSize([1000, 1000, 3, 7])
    print(result)
    result = s.minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(result)
