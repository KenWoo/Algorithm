from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(n, r, path):
            if not n and path not in r:
                r.append(path)
            else:
                for i in range(len(n)):
                    dfs(n[:i]+n[i+1:], r, path+[n[i]])
        dfs(nums, res, [])
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.permuteUnique([1,1,2])
    print(result)