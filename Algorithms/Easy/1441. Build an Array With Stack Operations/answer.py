from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        index = 0
        for i in range(1, n+1):
            res.append('Push')
            if i == target[index]:
                index += 1
            else:
                res.append('Pop')
            if index >= len(target):
                break
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.buildArray([1, 2], 4)
    print(result)
