from typing import List


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        map = ["0", "1", "2", "3", "4", "5", "6", "7",
               "8", "9", "a", "b", "c", "d", "e", "f"]
        hex = ""
        for _ in range(8):
            hex = map[num & 0xf] + hex
            num = num >> 4

        return hex.lstrip("0")


if __name__ == "__main__":
    s = Solution()
    result = s.toHex(-1)
    print(result)
