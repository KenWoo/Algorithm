from typing import List
import collections


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dict = collections.Counter(S)
        res = 0
        for j in J:
            if j in dict:
                res += dict[j]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.numJewelsInStones("z", "ZZ")
    print(result)
