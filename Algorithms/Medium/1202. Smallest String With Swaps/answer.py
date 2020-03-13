from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        fa = list(range(N))

        def find(x):
            while x != fa[x]:
                fa[x] = fa[fa[x]]
                x = fa[x]
            return x

        def union(a, b):
            aa, bb = find(a), find(b)
            fa[aa] = bb

        for a, b in pairs:
            union(a, b)
        dict = {}
        for i in range(N):
            key = find(i)
            dict.setdefault(key, [])
            dict[key].append(i)
        res = [''] * N
        for i in dict:
            ss = sorted(''.join([s[j] for j in dict[i]]))
            for k, p in zip(dict[i], ss):
                res[k] = p
        return ''.join(res)


if __name__ == "__main__":
    s = Solution()
    result = s.smallestStringWithSwaps("dcab",  [[0, 3], [1, 2]])
    print(result)
