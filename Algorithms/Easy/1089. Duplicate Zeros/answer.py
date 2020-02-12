from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        N = len(arr)
        i = 0
        while i < N:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop()
                i += 2
            else:
                i += 1


if __name__ == "__main__":
    s = Solution()
    arr = [4, 1, 0, 0, 8, 0, 0, 3]
    s.duplicateZeros(arr)
    print(arr)
