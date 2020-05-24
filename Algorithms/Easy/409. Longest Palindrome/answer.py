from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        for i in s:
            dict.setdefault(i, 0)
            dict[i] += 1
        odd_count = even_count = 0
        for _, v in dict.items():
            if v % 2 == 0:
                even_count += v
            else:
                even_count += v - 1
                odd_count = 1
        return even_count + max(odd_count, 0)


if __name__ == "__main__":
    s = Solution()
    result = s.longestPalindrome("ccc")
    print(result)
