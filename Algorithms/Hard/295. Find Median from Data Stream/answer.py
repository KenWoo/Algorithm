from typing import List


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        N = len(self.arr)
        return (self.arr[N // 2 - 1] + self.arr[N // 2]) / 2 if N % 2 == 0 else self.arr[N // 2]


if __name__ == "__main__":
    pass
