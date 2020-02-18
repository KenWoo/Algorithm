from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        dict = {}
        for i in range(N-1):
            for j in range(i+1, N):
                key = nums[i]+nums[j]
                dict.setdefault(key, [])
                dict[key].append((i, j))
        res = set()
        for i in range(N-1):
            for j in range(i+1, N):
                k = target - nums[i] - nums[j]
                if k in dict:
                    for v in dict[k]:
                        if i > v[1]:
                            res.add((nums[v[0]], nums[v[1]], nums[i], nums[j]))
        return [list(x) for x in res]


if __name__ == "__main__":
    s = Solution()
    result = s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)
    print(result)
