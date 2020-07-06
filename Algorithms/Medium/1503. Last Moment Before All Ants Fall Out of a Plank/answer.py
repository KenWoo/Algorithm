from tying import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = 0
        for i in left:
            res = max(res, i)
        for i in right:
            res = max(res, n-i)
        return res
        
if __name__ == "__main__":
    pass