from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s)
        N = len(l)
        for i in range(N//2):
            l[i], l[N-i-1] = l[N-i-1], l[i]
        s = ''.join(l)
        l = s.split()
        N = len(l)
        for i in range(N//2):
            l[i], l[N-i-1] = l[N-i-1], l[i]
        return ' '.join(l)


if __name__ == "__main__":
    s = Solution()
    result = s.reverseWords("Let's take LeetCode contest")
    print(result)
