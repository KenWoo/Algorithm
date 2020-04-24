from typing import List


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        c = "1" * len(bin(N)[2:])
        b = N ^ int(c, 2)
        return b


if __name__ == "__main__":
    pass
