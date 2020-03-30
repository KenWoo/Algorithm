from typing import List


class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        res = num
        for i, x in enumerate(s):
            if x == '6':
                n = int(s[:i] + '9' + s[i+1:])
                res = max(res, n)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.maximum69Number(9996)
    print(result)
