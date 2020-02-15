from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A = []
        for i in range(0, len(moves), 2):
            A.append(moves[i])
        if self.checkSame(A):
            return "A"
        B = []
        for i in range(1, len(moves), 2):
            B.append(moves[i])
        if self.checkSame(B):
            return "B"
        return "Pending" if len(A) + len(B) < 9 else "Draw"

    def checkSame(self, moves: List[List[int]]) -> bool:
        if len(moves) < 3:
            return False
        rows = [m[0] for m in moves]
        cols = [m[1] for m in moves]
        dict = {}
        for r in rows:
            dict.setdefault(r, 0)
            dict[r] += 1
        max_r = max(dict.values())
        if max_r >= 3:
            return True

        dict.clear()
        for c in cols:
            dict.setdefault(c, 0)
            dict[c] += 1
        max_c = max(dict.values())
        if max_c >= 3:
            return True

        if [1, 1] in moves and ([0, 0] in moves and [2, 2] in moves or [0, 2] in moves and [2, 0] in moves):
            return True

        return False


if __name__ == "__main__":
    s = Solution()
    result = s.tictactoe([[0, 2], [1, 0], [2, 2], [1, 2], [
                         2, 0], [0, 0], [0, 1], [2, 1], [1, 1]])
    print(result)
