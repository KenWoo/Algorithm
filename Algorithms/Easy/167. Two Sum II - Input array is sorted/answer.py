from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f_index = 0
        s_index = len(numbers) - 1
        while f_index < s_index:
            sum = numbers[f_index] + numbers[s_index]
            if sum == target:
                return [f_index + 1, s_index + 1]
            elif sum < target:
                f_index += 1
            else:
                s_index -= 1


if __name__ == "__main__":
    s = Solution()
    result = s.twoSum([2, 7, 11, 15], 9)
    print(result)
