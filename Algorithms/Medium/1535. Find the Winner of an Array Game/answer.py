from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_val = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if arr[i] > max_val:
                max_val = arr[i]
                count = 1
            else:
                count += 1
            if count == k:
                break
        return max_val


if __name__ == "__main__":
    s = Solution()
    result = s.getWinner([1, 9, 8, 2, 3, 7, 6, 4, 5], 7)
    print(result)
