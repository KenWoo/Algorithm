from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res = []

        def dfs(c, d):
            if len(d) == 0:
                res.append(c)
            else:
                for l in phone[d[0]]:
                    dfs(c+l, d[1:])
        if digits:
            dfs('', digits)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.letterCombinations('23')
    print(result)
