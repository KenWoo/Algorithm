from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        res = []

        def dfs(start, target, vlist):
            if target == 0:
                return res.append(vlist)
            for i in range(start, N):
                if target < candidates[i]:
                    break
                dfs(i, target-candidates[i], vlist + [candidates[i]])
        dfs(0, target, [])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.combinationSum([2, 3, 5], 8)
    print(result)
