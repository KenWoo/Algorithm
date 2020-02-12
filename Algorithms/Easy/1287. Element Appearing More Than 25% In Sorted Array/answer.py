from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        quarter = N // 4
        i = 0
        while i < N:
            if i + quarter < N and arr[i+quarter] == arr[i]:
                return arr[i]
            i += 1

        return None


if __name__ == "__main__":
    s = Solution()
    result = s.findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10])
    print(result)
