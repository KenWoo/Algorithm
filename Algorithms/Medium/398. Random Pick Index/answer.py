from typing import List
from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.dict = {}
        for i in range(len(nums)):
            self.dict.setdefault(nums[i], [])
            self.dict[nums[i]].append(i)

    def pick(self, target: int) -> int:
        v = self.dict[target]
        N = len(v)
        index = randint(0, N-1)
        return v[index]


if __name__ == "__main__":
    s = Solution([1, 2, 3, 3, 3])
    print(s.pick(3))
