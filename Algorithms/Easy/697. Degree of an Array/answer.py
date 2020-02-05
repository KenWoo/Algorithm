from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        a_min = m = len(nums)
        if m == 0:
            return 0

        dict = {}
        items = {}
        for i in range(m):
            n = nums[i]
            if n not in dict:
                dict[n] = 1
                items[n] = [i]
            else:
                dict[n] += 1
                items[n].append(i)

        degree = max(dict.values())

        for k, v in dict.items():
            if v == degree:
                start = items[k][0]
                end = items[k][-1]
                a_min = min(end-start+1, a_min)

        return a_min


if __name__ == "__main__":
    s = Solution()
    result = s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
    print(result)
