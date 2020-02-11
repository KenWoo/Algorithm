from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        dict = {}
        for t in time:
            part1 = t % 60
            part2 = (60 - t % 60) % 60
            count += dict.get(part1, 0)
            dict.setdefault(part2, 0)
            dict[part2] += 1
        return count


if __name__ == "__main__":
    s = Solution()
    result = s.numPairsDivisibleBy60([30, 20, 150, 100, 40])
    print(result)
