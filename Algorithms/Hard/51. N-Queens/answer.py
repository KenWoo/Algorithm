from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def check(k, j):
            for i in range(k):
                if board[i] == j or abs(board[i]-j) == abs(k-i):
                    return False
            return True
        def dfs(depth, v):
            if depth == n:
                res.append(v)
                return
            else:
                for i in range(n):
                    if check(depth, i):
                        board[depth] = i
                        s = '.' * n
                        dfs(depth+1, v + [s[:i] + 'Q' + s[i+1:]])
        res = []
        board = [-1 for i in range(n)]
        dfs(0, [])
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.solveNQueens(4)
    print(result)