from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        m = len(seats)
        start = 0
        end = 1
        index = steps = 0
        while end < m:
            if seats[end] == 1:
                if seats[start] == 0:
                    if steps < end - start:
                        steps = end - start
                        index = start
                else:
                    pivot = (end - start) // 2
                    if steps < pivot:
                        steps = pivot
                        index = start + pivot
                start = end
            else:
                if seats[start] == 1:
                    if end == m - 1 and steps < end - start:
                        steps = end - start
                        index = end
            end += 1
        return steps


if __name__ == "__main__":
    s = Solution()
    result = s.maxDistToClosest([1, 0, 0, 0])
    print(result)
