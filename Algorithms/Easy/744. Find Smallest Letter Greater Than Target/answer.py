from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for l in letters:
            if l > target:
                return l
        return letters[0]


if __name__ == "__main__":
    s = Solution()
    result = s.nextGreatestLetter(["c", "f", "j"], "a")
    print(result)
