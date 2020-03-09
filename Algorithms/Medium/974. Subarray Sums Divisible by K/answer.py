from typing import List
import collections


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)
        count = collections.Counter(P)
        return sum(v*(v-1)//2 for v in count.values())


if __name__ == "__main__":
    s = Solution()
    result = s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5)
    print(result)
