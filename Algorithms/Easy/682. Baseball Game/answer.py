from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        res = 0
        for o in ops:
            if o == 'C' and stack:
                res -= int(stack[-1])
                stack.pop()
            else:
                if o == '+':
                    stack.append(int(stack[-1]) + int(stack[-2]))
                elif o == 'D':
                    stack.append(int(stack[-1]) * 2)
                else:
                    stack.append(o)
                res += int(stack[-1])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
    print(result)
