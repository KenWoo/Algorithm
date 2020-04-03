from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        res = set()
        for w in words:
            l = []
            for s in w:
                idx = ord(s)-ord('a')
                l.append(morse[idx])
            res.add(''.join(l))
        return len(res)


if __name__ == "__main__":
    s = Solution()
    result = s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    print(result)
