from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dict = {}
        for n in dominoes:
            ss = (n[0], n[1])
            if ss in dict:
                dict[ss] += 1
            elif ss[::-1] in dict:
                dict[ss[::-1]] += 1
            else:
                dict[ss] = 1
        count = 0
        for _, n in dict.items():
            count += n * (n-1) // 2
        return count

    def factorial(self, n):
        if n == 0:
            return 1
        f = 1
        for i in range(1, n+1):
            f *= i
        return f


if __name__ == "__main__":
    s = Solution()
    result = s.numEquivDominoPairs(
        [[2, 1], [1, 2], [1, 2], [1, 2], [2, 1], [1, 1], [1, 2], [2, 2]])
    print(result)
