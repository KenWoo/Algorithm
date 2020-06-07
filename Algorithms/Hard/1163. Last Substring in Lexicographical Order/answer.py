from typing import List


class Solution:
    def lastSubstring(self, s: str) -> str:
        max_i = 0
        index = 1
        N = len(s)
        while index < N:
            if s[index] > s[max_i]:
                max_i = index
                index += 1
            elif s[index] == s[max_i]:
                begin_index = index
                max_pos = max_i
                while index < N and max_pos < begin_index and s[index] == s[max_pos]:
                    index += 1
                    max_pos += 1
                if index >= N or max_pos >= begin_index:
                    continue
                if s[index] > s[max_pos]:
                    max_i = begin_index
            else:
                index += 1
        return s[max_i:]


if __name__ == "__main__":
    s = Solution()
    result = s.lastSubstring("abab")
    print(result)
