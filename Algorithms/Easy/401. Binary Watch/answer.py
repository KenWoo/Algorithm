from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        for i in range(12):
            for j in range(60):
                if bin(i).count('1') + bin(j).count('1') == num:
                    res.append(f'{i}:{j:02d}')
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.readBinaryWatch(1)
    print(result)
