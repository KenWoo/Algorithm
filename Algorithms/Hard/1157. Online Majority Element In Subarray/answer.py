from typing import List
import random
import bisect


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.nums = arr
        self.dict = {}
        for i in range(len(arr)):
            self.dict.setdefault(arr[i], [])
            self.dict[arr[i]].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        ran = right - left + 1
        for _ in range(20):
            idx = random.randint(0, len(self.nums)) % ran + left
            num = self.nums[idx]
            l = self.dict[num]
            idx1 = bisect.bisect_left(l, left)
            idx2 = bisect.bisect_right(l, right)
            diff = idx2 - idx1
            if diff >= threshold:
                return self.nums[idx]
        return -1


if __name__ == "__main__":
    majorityChecker = MajorityChecker([1, 1, 2, 2, 1, 1])
    print(majorityChecker.query(0, 5, 4))
    print(majorityChecker.query(0, 3, 3))
    print(majorityChecker.query(2, 3, 2))
