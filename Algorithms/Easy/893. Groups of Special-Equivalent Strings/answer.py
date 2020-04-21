from typing import List


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        s = set()
        for a in A:
            s.add(''.join(sorted(a[0::2]))+''.join(sorted(a[1::2])))
        return len(s)


if __name__ == "__main__":
    s = Solution()
    result = s.numSpecialEquivGroups(
        ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"])
    print(result)
