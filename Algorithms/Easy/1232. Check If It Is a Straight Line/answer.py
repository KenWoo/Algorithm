from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        f = coordinates[0]
        s = coordinates[1]
        radio = 0 if s[0] - f[0] == 0 else (s[1] - f[1]) / (s[0] - f[0])
        for i in range(2, len(coordinates)):
            f, s = coordinates[i-1], coordinates[i]
            r = 0 if s[0] - f[0] == 0 else (s[1] - f[1]) / (s[0] - f[0])
            if radio != r:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.checkStraightLine(
        [[-7, -3], [-7, -1], [-2, -2], [0, -8], [2, -2], [5, -6], [5, -5], [1, 7]])
    print(result)
