from typing import List

class Solution:
    def totalNQueens(self, n: int) -> int:
        def check(k, j):
            for i in range(k):
                if board[i] == j or abs(board[i]-j) == abs(k-i):
                    return False
            return True
        def dfs(depth):
            if depth == n:
                self.res += 1
                return
            else:
                for i in range(n):
                    if check(depth, i):
                        board[depth] = i
                        dfs(depth+1)
        self.res = 0
        board = [-1 for i in range(n)]
        dfs(0)
        return self.res        

if __name__ == "__main__":
    s = Solution()
    result = s.totalNQueens(4)
    print(result)