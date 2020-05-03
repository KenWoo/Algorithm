from typing import List


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.v = [-1] * 1000000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.v[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.v[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.v[key] = -1


if __name__ == "__main__":
    pass
