from typing import List


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        n1, n2 = len(num1), len(num2)
        index = 0
        res = []
        rem = 0
        while index < n1 and index < n2:
            n = int(num1[index]) + int(num2[index]) + rem
            rem = n // 10
            res.append(str(n % 10))
            index += 1
        while index < n1:
            n = rem + int(num1[index])
            rem = n // 10
            res.append(str(n % 10))
            index += 1
        while index < n2:
            n = rem + int(num2[index])
            rem = n // 10
            res.append(str(n % 10))
            index += 1
        if rem == 1:
            res.append('1')
        res = res[::-1]
        return ''.join(res)


if __name__ == "__main__":
    s = Solution()
    result = s.addStrings('999', '999')
    print(result)
