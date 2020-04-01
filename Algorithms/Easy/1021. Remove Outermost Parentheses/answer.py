from typing import List


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        stack = []
        l = r = 0
        for s in S:
            if s == '(':
                l += 1
            else:
                r += 1
            if l == r:
                l = r = 0
                res.extend(stack[1:])
                stack = []
            else:
                stack.append(s)
        return ''.join(res)


if __name__ == "__main__":
    s = Solution()
    result = s.removeOuterParentheses("()()")
    print(result)
