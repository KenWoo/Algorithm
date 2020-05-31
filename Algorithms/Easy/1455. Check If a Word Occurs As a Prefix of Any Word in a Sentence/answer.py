from typing import List


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.split()
        N = len(s)
        for i in range(N):
            if s[i].startswith(searchWord):
                return i + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    result = s.isPrefixOfWord("i love eating burger", "burg")
    print(result)
