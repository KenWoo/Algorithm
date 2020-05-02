from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = [0] * num_people
        index, cur = 0, 1
        while candies > 0:
            n[index % num_people] += min(cur, candies)
            candies -= cur
            index += 1
            cur += 1
        return n


if __name__ == "__main__":
    s = Solution()
    result = s.distributeCandies(7, 4)
    print(result)
