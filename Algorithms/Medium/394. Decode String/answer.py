from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [['', 1]]
        num = ''
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(['', int(num)])
                num = ''
            elif c == ']':
                st, k = stack.pop()
                stack[-1][0] += st * k
            else:
                stack[-1][0] += c
        return stack[0][0]
        
if __name__ == "__main__":
    s = Solution()
    result = s.decodeString("3[a]2[bc]")
    print(result)