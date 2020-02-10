from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        min_str = A[0]
        for i in range(1, len(A)):
            if len(A[i]) < len(min_str):
                min_str = A[i]
        dict = {}
        for n in min_str:
            if n not in dict:
                dict[n] = 1
            else:
                dict[n] += 1
        for k, v in dict.items():
            for s in A:
                dict[k] = min(len([x for x in s if x == k]), dict[k])
        res = []
        for k, v in dict.items():
            res += [k] * v
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.commonChars(["cool", "lock", "cook"])
    print(result)
