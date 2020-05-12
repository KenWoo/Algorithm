from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r-1, c)
                if r+1 < R:
                    dfs(r+1, c)
                if c >= 1:
                    dfs(r, c-1)
                if c+1 < C:
                    dfs(r, c+1)
        dfs(sr, sc)
        return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    s = Solution()
    result = s.floodFill(image, sr, sc, newColor)
    print(result)
