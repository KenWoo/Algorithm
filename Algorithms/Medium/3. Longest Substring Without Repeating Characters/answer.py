from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        ans = start = end = 0
        N = len(s)
        while start < N and end < N:
            if s[end] not in ss:
                ss.add(s[end])
                end += 1
                ans = max(ans, end - start)
            else:
                ss.remove(s[start])
                start += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    result = s.lengthOfLongestSubstring("bbb")
    print(result)
