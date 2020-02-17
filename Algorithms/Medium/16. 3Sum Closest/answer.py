from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if N < 3:
            return None
        nums.sort()
        diff = float("inf")
        res = float("-inf")
        for i in range(N):
            j = i + 1
            k = N - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                elif sum < target:
                    j += 1
                else:
                    k -= 1
                if abs(target - sum) < diff:
                    diff = abs(target - sum)
                    res = sum
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.threeSumClosest([0, 0, 0], 1)
    print(result)
