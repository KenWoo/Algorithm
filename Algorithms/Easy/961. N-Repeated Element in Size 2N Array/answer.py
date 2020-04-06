from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        s = set()
        for a in A:
            if a not in s:
                s.add(a)
            else:
                return a
        return -1


if __name__ == "__main__":
    s = Solution()
    result = s.repeatedNTimes([2, 1, 2, 5, 3, 2])
    print(result)
