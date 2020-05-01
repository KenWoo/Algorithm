from typing import List


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict = {}
        for c in text:
            dict.setdefault(c, 0)
            dict[c] += 1
        res = []
        for c in 'balon':
            if c in dict:
                v = dict[c]
                if c == 'l' or c == 'o':
                    v //= 2
                res.append(v)
        return 0 if len(res) != 5 else min(res)


if __name__ == "__main__":
    s = Solution()
    result = s.maxNumberOfBalloons("balloon")
    print(result)
