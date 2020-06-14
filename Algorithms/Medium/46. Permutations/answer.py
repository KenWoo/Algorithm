from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)

        def dfs(t, visited):
            if len(t) == N:
                res.append(t[:])
                return
            for i in range(N):
                if not visited[i]:
                    t.append(nums[i])
                    visited[i] = True
                    dfs(t, visited)
                    t.pop()
                    visited[i] = False
        dfs([], [False] * N)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.permute([1, 2, 3])
    print(result)
