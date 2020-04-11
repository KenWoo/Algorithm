from typing import List


class RecentCounter:

    def __init__(self):
        self.nums = []

    def ping(self, t: int) -> int:
        self.nums.append(t)
        N = len(self.nums)
        l, r = 0, N - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.nums[mid] < t-3000:
                l = mid + 1
            else:
                r = mid - 1
        return N - l


if __name__ == "__main__":
    s = RecentCounter()
    print(s.ping(1))
    print(s.ping(100))
    print(s.ping(3001))
    print(s.ping(3002))
