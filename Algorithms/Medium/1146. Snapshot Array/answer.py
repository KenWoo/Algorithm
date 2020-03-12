from typing import List


class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.dict = {}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if index >= 0 and index < self.length:
            self.dict[(index, self.snap_id)] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        while snap_id >= 0:
            if (index, snap_id) in self.dict:
                return self.dict[(index, snap_id)]
            else:
                snap_id -= 1
        return 0


if __name__ == "__main__":
    snapshotArr = SnapshotArray(2)
    snapshotArr.set(0, 12)
    print(snapshotArr.snap())
    print(snapshotArr.snap())
    print(snapshotArr.get(1, 0))
    print(snapshotArr.get(1, 2))
    print(snapshotArr.snap())
    print(snapshotArr.snap())
