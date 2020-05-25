from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ll = []
        for i in range(1, area // 2 + 1):
            if area % i == 0 and i >= area // i:
                ll.append((i, area // i))
        ll.append((area, 1))
        res, diff = [], float('inf')
        for l in ll:
            if l[0] - l[1] < diff:
                diff = l[0] - l[1]
                res = l
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.constructRectangle(6)
    print(result)
