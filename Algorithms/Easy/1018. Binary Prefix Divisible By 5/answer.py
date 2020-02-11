from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        l = []
        a = 0
        for n in A:
            a = a * 2 + n
            l.append(a % 5 == 0)
        return l


if __name__ == "__main__":
    s = Solution()
    result = s.prefixesDivBy5([1, 1, 0, 0, 0, 1, 0, 0, 1])
    print(result)
