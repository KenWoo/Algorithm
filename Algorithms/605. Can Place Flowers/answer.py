from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = []
        l.extend([0])
        l.extend(flowerbed)
        l.extend([0, 1])

        sum = count = 0
        for i in l:
            if i == 0:
                count += 1
            else:
                sum += (count - 1) // 2
                count = 0

        return sum >= n


if __name__ == "__main__":
    s = Solution()
    result = s.canPlaceFlowers([0, 1, 0, 0, 0, 1, 0, 0], 3)
    print(result)
