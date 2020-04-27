from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_s = sorted(stones, reverse=True)
        while len(sorted_s) > 1:
            if sorted_s[0] == sorted_s[1]:
                sorted_s = sorted_s[2:]
            else:
                sorted_s = sorted([sorted_s[0] - sorted_s[1]] +
                                  sorted_s[2:], reverse=True)
        return 0 if len(sorted_s) == 0 else sorted_s[0]


if __name__ == "__main__":
    s = Solution()
    result = s.lastStoneWeight([2, 7, 4, 1, 8, 1])
    print(result)
