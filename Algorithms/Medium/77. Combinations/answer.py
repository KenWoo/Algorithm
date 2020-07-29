from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(j, kk, temp):
            if kk == 0:
                res.append(temp)
            for i in range(j+1, n+1):
                dfs(i, kk-1, temp+[i])
        res = []
        dfs(0, k, [])
        return res
        
if __name__ == "__main__":
    s = Solution()
    result = s.combine(4, 2)
    print(result)