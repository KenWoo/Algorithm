from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        listA = A.split()
        dictA = {}
        for s in listA:
            dictA.setdefault(s, 0)
            dictA[s] += 1
        listB = B.split()
        dictB = {}
        for s in listB:
            dictB.setdefault(s, 0)
            dictB[s] += 1
        s1 = set(listA)
        s2 = set(listB)
        ss = s1 ^ s2
        res = []
        for s in ss:
            if (s in dictA and dictA[s] > 1) or (s in dictB and dictB[s] > 1):
                continue
            res.append(s)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.uncommonFromSentences(
        "apple apple", "sour")
    print(result)
