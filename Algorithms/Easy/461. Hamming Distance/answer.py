from typing import List


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def convert2bits(n):
            quotient, remainder = n, 0
            bits = []
            while quotient > 0:
                quotient = n // 2
                remainder = n % 2
                n = quotient
                bits.append(remainder)
            return bits
        bit_x = convert2bits(x)
        bit_y = convert2bits(y)
        x_len = len(bit_x)
        y_len = len(bit_y)
        max_len = max(x_len, y_len)
        if x_len != max_len:
            bit_x += [0] * (max_len - x_len)
        else:
            bit_y += [0] * (max_len - y_len)
        res = 0
        for i in range(max_len):
            if bit_x[i] != bit_y[i]:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.hammingDistance(1, 4)
    print(result)
