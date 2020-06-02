from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        dict = {}
        for s in paragraph.split():
            key = s.lower()
            dict.setdefault(key, 0)
            dict[key] += 1
        dict = {k: v for k, v in sorted(
            dict.items(), key=lambda item: -item[1])}
        for k, _ in dict.items():
            if k not in banned:
                return k
        return ''


if __name__ == "__main__":
    s = Solution()
    result = s.mostCommonWord(
        "a, a, a, a, b,b,b,c, c", ["a"])
    print(result)
