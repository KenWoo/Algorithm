from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        q = []
        for n in queries:
            dict = {}
            for s in n:
                dict.setdefault(s, 0)
                dict[s] += 1
            q.append(dict[min(dict.keys())])
        w = []
        for n in words:
            dict = {}
            for s in n:
                dict.setdefault(s, 0)
                dict[s] += 1
            w.append(dict[min(dict.keys())])
        w.sort(reverse=True)
        res = []
        for n in q:
            count = 0
            for s in w:
                if n >= s:
                    break
                count += 1
            res.append(count)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.numSmallerByFrequency(["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"], [
                                     "aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"])
    print(result)
