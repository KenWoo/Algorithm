from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for n in nums:
            dict.setdefault(n, 0)
            dict[n] += 1
        sorted_dict = sorted(dict.items(), key=lambda x: -x[1])
        res = []
        for i in range(k):
            res.append(sorted_dict[i][0])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.topKFrequent([1], 1)
    print(result)
