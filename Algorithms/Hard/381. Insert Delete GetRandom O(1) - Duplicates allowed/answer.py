from typing import List
from random import randint


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.dict.setdefault(val, set())
        self.dict[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.dict:
            return False
        idx = next(iter(self.dict[val]))
        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
        self.dict[val].remove(idx)
        N = len(self.nums)
        if idx < N-1:
            self.dict[self.nums[idx]].remove(N-1)
            self.dict[self.nums[idx]].add(idx)
        self.nums.pop()
        if len(self.dict[val]) == 0:
            del self.dict[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.nums[randint(0, len(self.nums) - 1)]


if __name__ == "__main__":
    collection = RandomizedCollection()
    collection.insert(1)
    collection.insert(1)
    collection.insert(2)
    collection.getRandom()
    collection.remove(1)
    collection.getRandom()
