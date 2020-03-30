from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        res = 0
        for i in range(N):
            l1 = l2 = r1 = r2 = 0
            for j in range(i-1, -1, -1):
                if rating[j] < rating[i]:
                    l1 += 1
                elif rating[j] > rating[i]:
                    l2 += 1
            for j in range(i+1, N):
                if rating[j] < rating[i]:
                    r1 += 1
                elif rating[j] > rating[i]:
                    r2 += 1
            res += l1 * r2 + l2 * r1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.numTeams([1, 2, 3, 4])
    print(result)
