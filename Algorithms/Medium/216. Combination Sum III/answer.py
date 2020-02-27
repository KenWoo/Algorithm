from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        res = []

        def dfs(start, target, vlist):
            if target == 0:
                if len(vlist) == k:
                    res.append(vlist)
                return
            for i in range(start, 9):
                if target < candidates[i]:
                    break
                dfs(i+1, target-candidates[i], vlist + [candidates[i]])
        dfs(0, n, [])

        return res


if __name__ == "__main__":
    s = Solution()
    result = s.combinationSum3(3, 9)
    print(result)
