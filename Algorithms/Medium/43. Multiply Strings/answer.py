from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        M, N = len(num1), len(num2)
        tmp = [0] * (M + N)
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i+j, i+j+1
                s = mul + tmp[p2]
                tmp[p1] += s // 10
                tmp[p2] = s % 10
        res = []
        for i in range(len(tmp)):
            if res or tmp[i] != 0:
                res.append(str(tmp[i]))
        return '0' if not res else ''.join(res)


if __name__ == "__main__":
    s = Solution()
    result = s.multiply('123', '456')
    print(result)
