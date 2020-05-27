from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or
                    rec1[3] <= rec2[1] or
                    rec1[0] >= rec2[2] or
                    rec1[1] >= rec2[3])


if __name__ == "__main__":
    s = Solution()
    result = s.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3])
    print(result)
