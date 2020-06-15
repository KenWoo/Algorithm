from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict = {}
        for a in arr:
            dict.setdefault(a, 0)
            dict[a] += 1
        sorted_dict = sorted(dict.items(), key=lambda x: x[1])
        count = 0
        res = 0
        for item in sorted_dict:
            if count >= k:
                res += 1
            else:
                count += item[1]
                if count > k:
                    res += 1
        return res

if __name__ == "__main__":
    s = Solution()
    result = s.findLeastNumOfUniqueInts([5,5,4], 1)
    print(result)