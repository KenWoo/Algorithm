from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        res = [0] * k
        for a in arr:
            res[(a % k + k) % k] +=1
        for i in range(1, k):
            if res[i] != res[k-i]:
                return False
        return res[0] % 2 == 0

if __name__ == "__main__":
    s = Solution()
    result = s.canArrange([1,2,3,4,5,6], 10)
    print(result)