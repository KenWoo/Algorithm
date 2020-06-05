from typing import List


class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


if __name__ == "__main__":
    s = Solution()
    result = s.countSegments("Hello, my name is John")
    print(result)
