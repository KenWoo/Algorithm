from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        N = len(nums)
        oddNums, oddMax = nums[:], 0
        for i in range(1, N):
            if i % 2 == 0:
                if oddNums[i] >= oddNums[i-1]:
                    oddMax += oddNums[i] - oddNums[i-1] + 1
                    oddNums[i] = oddNums[i-1] - 1
            else:
                if oddNums[i] <= oddNums[i-1]:
                    oddMax += oddNums[i-1] - oddNums[i] + 1
                    oddNums[i-1] = oddNums[i] - 1
        evenNums, evenMax = nums[:], 0
        for i in range(1, N):
            if i % 2 == 0:
                if evenNums[i] <= evenNums[i-1]:
                    evenMax += evenNums[i-1]-evenNums[i] + 1
                    evenNums[i-1] = evenNums[i] - 1
            else:
                if evenNums[i] >= evenNums[i-1]:
                    evenMax += evenNums[i] - evenNums[i-1] + 1
                    evenNums[i] = evenNums[i-1] - 1
        return min(oddMax, evenMax)


if __name__ == "__main__":
    s = Solution()
    result = s.movesToMakeZigzag([9, 6, 1, 6, 2])
    print(result)
