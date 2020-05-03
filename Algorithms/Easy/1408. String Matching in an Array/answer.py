from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        N = len(words)
        res = set()
        for i in range(N-1):
            for j in range(i+1, N):
                if words[j].find(words[i]) != -1:
                    res.add(words[i])
        return list(res)


if __name__ == "__main__":
    s = Solution()
    result = s.stringMatching(["leetcode", "et", "code"])
    print(result)
