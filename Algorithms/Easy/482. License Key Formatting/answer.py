from typing import List


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        arr = []
        for s in S:
            if s != '-':
                arr.append(s.upper())
        res = []
        N = len(arr)
        rem = N % K
        i = 0
        if rem > 0:
            res.extend(arr[0:rem])
            i = rem
            if i < N:
                res.append('-')
        while i < N:
            res.extend(arr[i:i+K])
            if i+K < N:
                res.append('-')
            i += K
        return ''.join(res)


if __name__ == "__main__":
    s = Solution()
    result = s.licenseKeyFormatting("2", 2)
    print(result)
