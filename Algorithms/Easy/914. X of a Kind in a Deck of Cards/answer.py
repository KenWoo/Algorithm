from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dict = {}
        for n in deck:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1

        N = len(deck)
        for x in range(2, N+1):
            if N % x == 0:
                if all(v % x == 0 for v in dict.values()):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    result = s.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1])
    print(result)
