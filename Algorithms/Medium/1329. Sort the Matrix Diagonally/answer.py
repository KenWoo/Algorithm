from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])
        for j in range(C-2, -1, -1):
            arr = []
            cur_r, cur_c = 0, j
            while cur_r < R and cur_c < C:
                arr.append(mat[cur_r][cur_c])
                cur_r, cur_c = cur_r+1, cur_c+1
            arr.sort()
            cur_r, cur_c, k = 0, j, 0
            while cur_r < R and cur_c < C:
                mat[cur_r][cur_c] = arr[k]
                cur_r, cur_c = cur_r+1, cur_c+1
                k += 1
        for i in range(1, R-1):
            arr = []
            cur_r, cur_c = i, 0
            while cur_r < R and cur_c < C:
                arr.append(mat[cur_r][cur_c])
                cur_r, cur_c = cur_r+1, cur_c+1
            arr.sort()
            cur_r, cur_c, k = i, 0, 0
            while cur_r < R and cur_c < C:
                mat[cur_r][cur_c] = arr[k]
                cur_r, cur_c = cur_r+1, cur_c+1
                k += 1
        return mat


if __name__ == "__main__":
    s = Solution()
    result = s.diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
    print(result)
