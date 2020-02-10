from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        N = 8
        R = ()
        B = []
        p = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == "R":
                    R = (i, j)
                elif board[i][j] == 'B':
                    B.append((i, j))
                elif board[i][j] == 'p':
                    p.append((i, j))

        count = 0
        c_B = [n[1] for n in B if n[0] == R[0]]
        c_p = [n[1] for n in p if n[0] == R[0]]
        i = R[0]
        while i >= 0:
            if i in c_B:
                break
            if i in c_p:
                count += 1
                break
            i -= 1
        i = R[0]
        while i < 8:
            if i in c_B:
                break
            if i in c_p:
                count += 1
                break
            i += 1

        r_B = [n[0] for n in B if n[1] == R[1]]
        r_p = [n[0] for n in p if n[1] == R[1]]
        i = R[1]
        while i >= 0:
            if i in r_B:
                break
            if i in r_p:
                count += 1
                break
            i -= 1
        i = R[1]
        while i < 8:
            if i in r_B:
                break
            if i in r_p:
                count += 1
                break
            i += 1

        return count


if __name__ == "__main__":
    s = Solution()
    result = s.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", "p", "p", ".", ".", ".", "."], [".", "p", "p", "R", ".", "p", ".", "p"], [
                               ".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", "p", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]])
    print(result)
