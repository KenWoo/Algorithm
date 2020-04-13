from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        for a in arr:
            res.append((str(bin(a)).count('1'), a))
        res.sort(key=lambda x: (x[0], x[1]))
        return [x[1] for x in res]


if __name__ == "__main__":
    s = Solution()
    result = s.sortByBits([2, 3, 5, 7, 11, 13, 17, 19])
    print(result)
