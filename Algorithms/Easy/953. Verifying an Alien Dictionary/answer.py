from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {c: i for i, c in enumerate(order)}
        N = len(words)
        for i in range(N-1):
            w1 = words[i]
            w2 = words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if dict[w1[j]] > dict[w2[j]]:
                        return
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.isAlienSorted(["hello", "leetcode"],
                             "hlabcdefgijkmnopqrstuvwxyz")
    print(result)
