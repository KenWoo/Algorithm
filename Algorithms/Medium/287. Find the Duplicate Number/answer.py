from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t = h = nums[0]
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h:
                break
        p1 = nums[0]
        p2 = t
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1


if __name__ == "__main__":
    s = Solution()
    result = s.findDuplicate([3, 1, 3, 4, 2])
    print(result)
