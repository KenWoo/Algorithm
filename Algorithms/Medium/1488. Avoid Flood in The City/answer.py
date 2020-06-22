from typing import List
import collections
import heapq


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N = len(rains)
        dic = collections.defaultdict(list)
        res = [-1] * N
        to_empty = []

        for i, lake in enumerate(rains):
            dic[lake].append(i)

        for i in range(N):
            lake = rains[i]
            if lake:
                if dic[lake] and dic[lake][0] < i:
                    return []
                if dic[lake] and len(dic[lake]) > 1:
                    heapq.heappush(to_empty, dic[lake][1])
            else:
                if to_empty:
                    res[i] = rains[heapq.heappop(to_empty)]
                    dic[res[i]].pop(0)
                else:
                    res[i] = 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.avoidFlood([1, 2, 0, 0, 2, 1])
    print(result)
