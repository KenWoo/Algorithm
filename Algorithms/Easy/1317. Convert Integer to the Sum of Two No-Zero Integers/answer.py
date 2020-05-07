from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        f, s = 1, n-1
        while f <= s:
            if str(f).find('0') == -1 and str(s).find('0') == -1:
                return [f, s]
            f += 1
            s -= 1


if __name__ == "__main__":
    s = Solution()
    result = s.getNoZeroIntegers(69)
    print(result)
