from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        res = []

        def dfs(start, target, vlist):
            if target == 0:
                return res.append(vlist)
            for i in range(start, N):
                if target < candidates[i]:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, target-candidates[i], vlist+[candidates[i]])
        dfs(0, target, [])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(result)
