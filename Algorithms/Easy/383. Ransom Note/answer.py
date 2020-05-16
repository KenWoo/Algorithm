from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for m in magazine:
            dict.setdefault(m, 0)
            dict[m] += 1
        for r in ransomNote:
            if r in dict and dict[r] != 0:
                dict[r] -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.canConstruct(ransomNote="aa", magazine="aab")
    print(result)
