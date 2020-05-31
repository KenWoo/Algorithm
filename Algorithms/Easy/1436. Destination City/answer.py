from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict = {}
        for p in paths:
            src, dst = p[0], p[1]
            dict.setdefault(src, 0)
            dict.setdefault(dst, 0)
            dict[src] += 1
        for k, v in dict.items():
            if v == 0:
                return k
        return ''


if __name__ == "__main__":
    s = Solution()
    result = s.destCity(
        [["A", "Z"]])
    print(result)
