from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res


if __name__ == "__main__":
    s = Solution()
    result = s.merge([[2, 3], [4, 5], [6, 7], [1, 10]])
    print(result)
