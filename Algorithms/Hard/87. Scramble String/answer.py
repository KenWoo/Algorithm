from typing import List


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        sl_len = len(s1)
        f = self.isScramble
        for i in range(1, sl_len):
            if f(s1[i:], s2[i:]) and f(s1[:i], s2[:i]):
                return True
            if f(s1[i:], s2[:sl_len - i]) and f(s1[:i], s2[sl_len - i:]):
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    result = s.isScramble('great', 'rgeat')
    print(result)
