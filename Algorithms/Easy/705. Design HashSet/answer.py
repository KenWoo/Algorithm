from typing import List


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.v = [0] * 1000000

    def add(self, key: int) -> None:
        self.v[key] = 1

    def remove(self, key: int) -> None:
        self.v[key] = 0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.v[key] == 1


if __name__ == "__main__":
    pass
