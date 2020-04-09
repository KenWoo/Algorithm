from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l, r = 0, len(S)
        res = []
        for s in S:
            if s == 'I':
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
        res.append(l)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.diStringMatch("IIID")
    print(result)
