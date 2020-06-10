from typing import List


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        N = len(text)
        res = set()
        for i in range(N):
            j = 1
            while j <= (N-i)//2:
                if text[i:i+j] == text[i+j:i+j+j]:
                    res.add(text[i:i+j])
                j += 1
        return len(res)


if __name__ == "__main__":
    s = Solution()
    result = s.distinctEchoSubstrings("abcabcabc")
    print(result)
