from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False

        m = len(board)
        n = len(board[0])

        def search(row: int, col: int, word: str, hash: set) -> bool:
            if not word:
                return True
            if row < 0 or row >= m:
                return False
            if col < 0 or col >= n:
                return False
            if (row, col) in hash:
                return False
            if word[0] != board[row][col]:
                return False
            else:
                hash.add((row, col))

            n_word = word[1:]
            res = False
            res = res or search(row, col-1, n_word, hash)
            res = res or search(row, col+1, n_word, hash)
            res = res or search(row-1, col, n_word, hash)
            res = res or search(row+1, col, n_word, hash)
            if not res:
                hash.remove((row, col))
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if search(i, j, word, set()):
                        return True
        return False


if __name__ == "__main__":
    s = Solution()
    result = s.exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
                     "ABCESEEEFS")
    print(result)
