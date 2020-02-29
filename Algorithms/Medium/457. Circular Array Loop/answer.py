from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def advance(i, nums):
            n = len(nums)
            return (((nums[i] + i) % n) + n) % n

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            slow, fast, val = i, advance(i, nums), nums[i]
            while val * nums[fast] > 0 and val * nums[advance(fast, nums)] > 0:
                if slow == fast:
                    if slow == advance(slow, nums):
                        break
                    else:
                        return True
                slow = advance(slow, nums)
                fast = advance(advance(fast, nums), nums)
            slow = i
            while val * nums[slow] > 0:
                next = advance(slow, nums)
                nums[slow] = 0
                slow = next
        return False


if __name__ == "__main__":
    s = Solution()
    result = s.circularArrayLoop([-1, 2])
    print(result)
