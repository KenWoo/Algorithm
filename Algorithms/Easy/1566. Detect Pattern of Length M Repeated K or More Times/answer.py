from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        N = len(arr)
        count = 0
        for i in range(N-m):
            if arr[i] == arr[i+m]:
                count += 1
            else:
                count = 0
            if count == m * (k - 1):
                return True
        return False


if __name__ == "__main__":
    pass
