from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        dict = {}
        i = 0
        rank = 0
        while i < len(arr):
            if sorted_arr[i] not in dict:
                rank += 1
                dict[sorted_arr[i]] = rank
            i += 1
        res = []
        for n in arr:
            res.append(dict[n])
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12])
    print(result)
