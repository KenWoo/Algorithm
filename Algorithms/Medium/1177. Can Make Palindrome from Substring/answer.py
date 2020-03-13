from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        grid = [[0] * len(s) for _ in range(26)]
        count = [0] * 26

        for i, v in enumerate(s):
            for j in range(26):
                grid[j][i] = grid[j][i-1]
            inx = ord(v) - ord('a')
            count[inx] += 1
            grid[inx][i] = count[inx]

        res = []
        for left, right, k in queries:
            diff = 0
            for i in range(26):
                if left > 0 and (grid[i][right] - grid[i][left-1]) % 2 != 0:
                    diff += 1
                elif left == 0 and grid[i][right] % 2 != 0:
                    diff += 1
            if diff == 1 or diff // 2 <= k:
                res.append(True)
            else:
                res.append(False)

        return res


if __name__ == "__main__":
    s = Solution()
    result = s.canMakePaliQueries(
        "abcda", [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]])
    print(result)
