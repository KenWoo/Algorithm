from typing import List
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)-1):
            if arr[i+1] - arr[i] != diff:
                return False
        return True
        
if __name__ == "__main__":
    s = Solution()
    result = s.canMakeArithmeticProgression([4,5,1])
    print(result)