from typing import List


class Solution:
    def checkRecord(self, s: str) -> bool:
        isAbsent = False
        count = 0
        for i in s:
            if i == 'A':
                count += 1
            if count > 1:
                isAbsent = True
                break
        isLate = False
        for i in range(2, len(s)):
            if s[i-2] == 'L' and s[i-1] == 'L' and s[i] == 'L':
                isLate = True
                break
        return not(isAbsent or isLate)


if __name__ == "__main__":
    s = Solution()
    result = s.checkRecord("PPALLP")
    print(result)
