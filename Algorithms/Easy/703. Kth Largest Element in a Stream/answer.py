from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]


if __name__ == "__main__":
    c = KthLargest(3, [4, 5, 8, 2])
    print(c.add(3))
    print(c.add(5))
