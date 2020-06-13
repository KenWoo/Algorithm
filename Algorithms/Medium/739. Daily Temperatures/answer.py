from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        nxt = [float('inf')] * 102
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            warmer_index = min(nxt[t] for t in range(T[i]+1, 102))
            if warmer_index < float('inf'):
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans


if __name__ == "__main__":
    s = Solution()
    result = s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(result)
