from typing import List


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        def check(s, i):
            for c in s:
                i = S.find(c, i) + 1
                if not i:
                    return False
            return True
        return sum((check(word, 0) for word in words))


if __name__ == "__main__":
    s = Solution()
    result = s.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"])
    print(result)
