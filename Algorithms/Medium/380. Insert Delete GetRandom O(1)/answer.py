from typing import List
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            last, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last] = last, idx
            self.list.pop()
            del self.dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)


if __name__ == "__main__":
    s = RandomizedSet()
    s.insert(1)
    print(s.list)
    print(s.getRandom())
