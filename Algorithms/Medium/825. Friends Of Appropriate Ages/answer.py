from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        dict = {}
        for age in ages:
            if age not in dict:
                dict.setdefault(age, 0)
            dict[age] += 1
        res = 0
        for ageA, countA in dict.items():
            for ageB, countB in dict.items():
                if ageA * 0.5 + 7 >= ageB:
                    continue
                if ageA < ageB:
                    continue
                if ageA < 100 < ageB:
                    continue
                res += countA * countB
                if ageA == ageB:
                    res -= countA
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.numFriendRequests([16, 16, 16])
    print(result)
