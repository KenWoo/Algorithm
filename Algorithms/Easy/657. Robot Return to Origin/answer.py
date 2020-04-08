from typing import List


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dict = {}
        for m in moves:
            dict.setdefault(m, 0)
            dict[m] += 1
        l = dict.get('L', 0)
        r = dict.get('R', 0)
        u = dict.get('U', 0)
        d = dict.get('D', 0)
        return l == r and u == d


if __name__ == "__main__":
    s = Solution()
    result = s.judgeCircle("UD")
    print(result)
