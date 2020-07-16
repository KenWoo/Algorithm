from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        res = []
        dict = {}
        N, W, w = len(s), len(words), len(words[0])
        for i in range(W):
            dict.setdefault(words[i], 0)
            dict[words[i]] += 1
        for i in range(N-W*w+1):
            cur, j = {}, 0
            while j < W:
                word = s[i+j*w:i+(j+1)*w]
                if not word in dict:
                    break
                if not word in cur:
                    cur[word] = 1
                else:
                    cur[word] += 1
                if cur[word] > dict[word]:
                    break
                j += 1
            if j == W:
                res.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findSubstring("barfoothefoobarman", ["foo","bar"])
    print(result)