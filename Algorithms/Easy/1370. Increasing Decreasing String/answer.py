from typing import List


class Solution:
    def sortString(self, s: str) -> str:
        dict = {}
        for n in s:
            dict.setdefault(n, 0)
            dict[n] += 1
        sorted_key = sorted(dict.keys())
        N = len(sorted_key)
        res = []
        while len(res) != len(s):
            for i in range(N):
                k = sorted_key[i]
                if dict[k] != 0:
                    dict[k] -= 1
                    res.append(k)
            for i in range(N-1, -1, -1):
                k = sorted_key[i]
                if dict[k] != 0:
                    dict[k] -= 1
                    res.append(k)
        return ''.join(res)


if __name__ == "__main__":
    s = Solution()
    result = s.sortString("leetcode")
    print(result)
