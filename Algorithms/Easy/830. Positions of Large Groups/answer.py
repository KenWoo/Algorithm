from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        l = []
        start = end = 0
        while start < len(S):
            while end < len(S) and S[start] == S[end]:
                end += 1
            if end - start >= 3:
                l.append([start, end - 1])
            start = end
        return l


if __name__ == "__main__":
    s = Solution()
    result = s.largeGroupPositions("abc")
    print(result)
