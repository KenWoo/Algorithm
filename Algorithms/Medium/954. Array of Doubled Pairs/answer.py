from typing import List


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        dict = {}
        for a in A:
            if a*2 in dict:
                dict[a*2] -= 1
                if dict[a*2] == 0:
                    del(dict[a*2])
            elif a/2 in dict:
                dict[a/2] -= 1
                if dict[a/2] == 0:
                    del(dict[a/2])
            else:
                dict[a] = dict.setdefault(a, 0) + 1
        return len(dict) == 0


if __name__ == "__main__":
    s = Solution()
    result = s.canReorderDoubled([-1, 4, 6, 8, -4, 6, -6, 3, -2, 3, -3, -8])
    print(result)
