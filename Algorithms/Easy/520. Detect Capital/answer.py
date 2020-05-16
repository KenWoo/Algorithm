from typing import List


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word == (word[0].upper() + word[1:].lower())


if __name__ == "__main__":
    s = Solution()
    result = s.detectCapitalUse("Usa")
    print(result)
