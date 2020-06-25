from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N, n = len(s), len(p)
        res = []
        pp = sorted(p)
        for i in range(0, N-n+1):
            if sorted(s[i:i+n]) == pp:
                res.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findAnagrams("cbaebabacd", "abc")
    print(result)
