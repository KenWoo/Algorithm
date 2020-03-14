from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        right = count = 0
        for i in range(len(light)):
            right = max(right, light[i])
            if right == i + 1:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    result = s.numTimesAllBlue([2, 1, 3, 5, 4])
    print(result)
    result = s.numTimesAllBlue([3, 2, 4, 1, 5])
    print(result)
    result = s.numTimesAllBlue([4, 1, 2, 3])
    print(result)
    result = s.numTimesAllBlue([2, 1, 4, 3, 6, 5])
    print(result)
    result = s.numTimesAllBlue([1, 2, 3, 4, 5, 6])
    print(result)
