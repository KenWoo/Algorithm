from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        a = b = count1 = count2 = 0
        for n in nums:
            if n == a:
                count1 += 1
            elif n == b:
                count2 += 1
            elif count1 == 0:
                a = n
                count1 = 1
            elif count2 == 0:
                b = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = count2 = 0
        for n in nums:
            if n == a:
                count1 += 1
            elif n == b:
                count2 += 1
        if count1 > len(nums) // 3:
            res.append(a)
        if count2 > len(nums) // 3:
            res.append(b)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.majorityElement([1, 1, 1, 3, 3, 2, 2, 2])
    print(result)
