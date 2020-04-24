from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1 = "qwertyuiop"
        l2 = "asdfghjkl"
        l3 = "zxcvbnm"
        res = []
        for w in words:
            tmp = []
            for c in w:
                c = c.lower()
                if c in l1:
                    tmp.append(0)
                elif c in l2:
                    tmp.append(1)
                elif c in l3:
                    tmp.append(2)
            tmp.sort()
            if tmp[0] == tmp[-1]:
                res.append(w)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(result)
