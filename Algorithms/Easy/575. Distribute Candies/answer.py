from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        N = len(candies)
        dict = {}
        for c in candies:
            dict.setdefault(c, 0)
            dict[c] += 1
        count = 0
        for k in dict.keys():
            if count == N//2:
                break
            if dict[k] > 0:
                count += 1
                dict[k] -= 1
        return count


if __name__ == "__main__":
    s = Solution()
    result = s.distributeCandies([1, 2, 3, 1, 2, 3])
    print(result)
