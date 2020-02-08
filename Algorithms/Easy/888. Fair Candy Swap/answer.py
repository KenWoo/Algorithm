from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A = sum(A)
        sum_B = sum(B)
        set_B = set(B)
        for a in A:
            if a + (sum_B - sum_A) // 2 in set_B:
                return [a, a + (sum_B - sum_A) // 2]


if __name__ == "__main__":
    s = Solution()
    result = s.fairCandySwap([1, 2, 5], [2, 4])
    print(result)
