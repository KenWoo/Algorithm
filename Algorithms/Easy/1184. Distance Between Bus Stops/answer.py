from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        part1 = distance[start:destination]
        part2 = distance[0:start] + distance[destination:]
        return min(sum(part1), sum(part2))


if __name__ == "__main__":
    s = Solution()
    result = s.distanceBetweenBusStops([7, 10, 1, 12, 11, 14, 5, 0], 7, 2)
    print(result)
