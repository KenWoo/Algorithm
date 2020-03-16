from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        N, cur = len(intervals), 0
        while cur < N and intervals[cur][1] < newInterval[0]:
            res.append(intervals[cur])
            cur += 1
        while cur < N and intervals[cur][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[cur][0])
            newInterval[1] = max(newInterval[1], intervals[cur][1])
            cur += 1
        res.append(newInterval)
        while cur < N:
            res.append(intervals[cur])
            cur += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    print(result)
