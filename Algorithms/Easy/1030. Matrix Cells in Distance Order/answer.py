from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dict = {}
        for r in range(R):
            for c in range(C):
                dict[(r, c)] = abs(r-r0) + abs(c-c0)
        sorted_dict = sorted(dict.items(), key=lambda item: item[1])
        return [list(x[0]) for x in sorted_dict]


if __name__ == "__main__":
    s = Solution()
    result = s.allCellsDistOrder(2, 3, 1, 2)
    print(result)
