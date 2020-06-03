from typing import List


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, m, n = 0, len(name), len(typed)
        for j in range(n):
            if i < m and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
        return i == m


if __name__ == "__main__":
    s = Solution()
    result = s.isLongPressedName("alex", "alexxr")
    print(result)
