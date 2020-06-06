from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = -1
        for i in range(4):
            for j in range(4):
                if i != j:
                    for k in range(4):
                        if i != k and j != k:
                            l = 6 - i - j - k
                            hours = 10 * A[i] + A[j]
                            minutes = 10 * A[k] + A[l]
                            if hours < 24 and minutes < 59:
                                ans = max(ans, 60 * hours + minutes)
        return '' if ans == -1 else f'{ans // 60:02}:{ans % 60:02}'


if __name__ == "__main__":
    s = Solution()
    result = s.largestTimeFromDigits([0, 0, 0, 0])
    print(result)
