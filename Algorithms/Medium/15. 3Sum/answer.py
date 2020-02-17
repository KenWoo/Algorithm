from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        if N < 3:
            return res
        nums.sort()
        for i in range(N):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = N - 1
            while j < k:
                a = nums[i]
                b = nums[j]
                c = nums[k]
                if b + c == -a:
                    res.append([a, b, c])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                elif b + c > -a:
                    k -= 1
                else:
                    j += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(result)
