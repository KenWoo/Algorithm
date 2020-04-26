from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return ['']
        res = ['']
        for s in S:
            if s.isalpha():
                res = [i+j for i in res for j in (s.upper(), s.lower())]
            else:
                res = [i+s for i in res]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.letterCasePermutation("a1b2")
    print(result)
