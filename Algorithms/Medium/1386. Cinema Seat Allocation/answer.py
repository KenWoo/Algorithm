from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        dict = {}
        for cell in reservedSeats:
            r, c = cell[0], cell[1]
            if c in [1, 10]:
                continue
            dict.setdefault(r-1, [])
            dict[r-1].append(c-1)
        res = 0
        for v in dict.values():
            s1 = s2 = s3 = 0
            for c in v:
                if c in [1, 2, 3, 4]:
                    s1 += 1
                if c in [3, 4, 5, 6]:
                    s2 += 1
                if c in [5, 6, 7, 8]:
                    s3 += 1
            if s1 == 0 or s2 == 0 or s3 == 0:
                res += 1
        N = len(dict.keys())
        res += (n - N) * 2
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maxNumberOfFamilies(
        3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]])
    print(result)
