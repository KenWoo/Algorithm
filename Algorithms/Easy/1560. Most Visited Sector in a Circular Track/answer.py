from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        res = []
        s, e = rounds[0], rounds[len(rounds)-1]
        if s > e:
            for i in range(1, e+1):
                res.append(i)
            for i in range(s, n+1):
                res.append(i)
        else:
            for i in range(s, e+1):
                res.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.mostVisited(4, [1, 3, 1, 2])
    print(result)
