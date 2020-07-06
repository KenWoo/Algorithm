from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        L1 = len(word1)
        L2 = len(word2)
        if L1 == 0:
            return L2
        if L2 == 0:
            return L1
        arr = [[0 for _ in range(L2+1)] for _ in range(L1+1)]
        for i in range(1, L1+1):
            arr[i][0] = i
        for i in range(1, L2+1):
            arr[0][i] = i
        if word1[0] != word2[0]:
            arr[1][1] = 1
        if L1 >= 1 and L2 >= 1:
            for i in range(1, L1+1):
                for j in range(1, L2+1):
                    arr[i][j] = min(arr[i-1][j]+1, arr[i][j-1]+1, arr[i-1][j-1]+int(word1[i-1] != word2[j-1]))
        return arr[L1][L2]

if __name__ == "__main__":
    pass