from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
        
if __name__ == "__main__":
    s = Solution()
    result = s.average( [4000,3000,1000,2000])
    print(result)