from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for n in arr:
            if n / 2 in s or n * 2 in s:
                return True
            s.add(n)
        return False


if __name__ == "__main__":
    s = Solution()
    result = s.checkIfExist(
        [10, 2, 5, 3, 4, 4])
    print(result)
