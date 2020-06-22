from typing import List

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res

        
if __name__ == "__main__":
    s = Solution()
    result = s.xorOperation(10, 5)
    print(result)