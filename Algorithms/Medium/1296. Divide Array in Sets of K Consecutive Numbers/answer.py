from typing import List
import collections


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if N % k != 0:
            return False
        dict = collections.Counter(nums)
        sorted_key = sorted(dict.keys())
        n = N // k
        while n > 0:
            start = 0
            for key in sorted_key:
                if dict[key] > 0:
                    start = key
                    break
            for key in range(start, start+k):
                if key in dict and dict[key] > 0:
                    dict[key] -= 1
                else:
                    return False
            n -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.isPossibleDivide([3, 3, 2, 2, 1, 1], 3)
    print(result)
