from typing import List


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        t = []
        for i in S:
            if s and i == '#':
                s.pop()
            if i != '#':
                s.append(i)
        for i in T:
            if t and i == '#':
                t.pop()
            if i != '#':
                t.append(i)
        return s == t


if __name__ == "__main__":
    s = Solution()
    result = s.backspaceCompare("ab#c", "b")
    print(result)
