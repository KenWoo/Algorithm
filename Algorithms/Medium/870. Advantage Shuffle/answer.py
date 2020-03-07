from typing import List
import collections


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)
        sortedB = sorted(B)
        advantage = {b: [] for b in B}
        not_advantage = []
        i = 0
        for a in sortedA:
            if a > sortedB[i]:
                advantage[sortedB[i]].append(a)
                i += 1
            else:
                not_advantage.append(a)

        res = []
        for b in B:
            if advantage[b]:
                res.append(advantage[b].pop())
            else:
                res.append(not_advantage.pop())
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.advantageCount([2, 7, 11, 15], [1, 10, 4, 11])
    print(result)
