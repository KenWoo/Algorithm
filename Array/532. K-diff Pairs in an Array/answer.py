from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = set()
        u = set()
        for n in nums:
            if n in s:
                u.add(n)
            s.add(n + k)

        return len(u)


if __name__ == "__main__":
    s = Solution()
    result = s.findPairs([1, 2, 3, 4, 5], 1)
    print(result)
