from typing import List


class Solution:
    def toLowerCase(self, str: str) -> str:
        return ''.join([chr(ord(s) + 32) if s >= 'A' and s <= 'Z' else s for s in str])


if __name__ == "__main__":
    s = Solution()
    result = s.toLowerCase("Hello")
    print(result)
