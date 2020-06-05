from typing import List
import math


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        N = math.ceil(math.log(1000000, 2))
        res = set()
        for i in range(N):
            for j in range(N):
                v = x ** i + y ** j
                if v <= bound:
                    res.add(v)
        return list(res)


if __name__ == "__main__":
    s = Solution()
    result = s.powerfulIntegers(2, 3, 10)
    print(result)
