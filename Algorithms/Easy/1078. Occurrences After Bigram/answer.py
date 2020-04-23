from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        l = text.split()
        N = len(l)
        res = []
        for i in range(N-2):
            if l[i] == first and l[i+1] == second:
                res.append(l[i+2])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.findOcurrences(
        "alice is a good girl she is a good student", "a", "good")
    print(result)
