from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for i, j, k in bookings:
            res[i-1] += k
            if j < n:
                res[j] -= k
        for i in range(1, n):
            res[i] += res[i-1]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)
    print(result)
