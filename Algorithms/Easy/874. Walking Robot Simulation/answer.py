from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        s = set(map(tuple, obstacles))
        res = 0
        for c in commands:
            if c == -2:
                di = (di - 1) % 4
            elif c == -1:
                di = (di + 1) % 4
            else:
                for _ in range(c):
                    if (x+dx[di], y+dy[di]) not in s:
                        x += dx[di]
                        y += dy[di]
                        res = max(res, x*x + y*y)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.robotSim([4, -1, 4, -2, 4], [[2, 4]])
    print(result)
