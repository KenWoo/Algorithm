from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dict = {}
        for c in licensePlate:
            if c.isalpha():
                c = c.lower()
                dict.setdefault(c, 0)
                dict[c] += 1
        res = []
        for w in words:
            w = w.lower()
            d = {}
            for s in w:
                d.setdefault(s, 0)
                d[s] += 1
            flag = True
            for k, v in dict.items():
                if k not in d or v > d[k]:
                    flag = False
                    break
            if flag:
                res.append(w)
        print(dict)
        res.sort(key=lambda x: len(x))
        return res[0]


if __name__ == "__main__":
    s = Solution()
    result = s.shortestCompletingWord(
        "GrC8950", ["measure", "other", "every", "base", "according", "level", "meeting", "none", "marriage", "rest"])
    print(result)
