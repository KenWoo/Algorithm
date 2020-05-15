from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def f(log):
            id, rest = log.split(" ", 1)
            return (0, rest, id) if rest[0].isalpha() else (1,)
        return sorted(logs, key=f)


if __name__ == "__main__":
    s = Solution()
    result = s.reorderLogFiles(
        ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
    print(result)
