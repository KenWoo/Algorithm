from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        N = len(startTime)
        res = 0
        for i in range(N):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    startTime = [4]
    endTime = [4]
    queryTime = 5
    result = s.busyStudent(startTime, endTime, queryTime)
    print(result)
