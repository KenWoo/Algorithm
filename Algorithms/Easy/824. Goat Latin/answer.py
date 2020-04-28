from typing import List


class Solution:
    def toGoatLatin(self, S: str) -> str:
        l = S.split()
        res = []
        for i in range(len(l)):
            s = l[i]
            if s[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                s += 'ma'
            else:
                s = s[1:] + s[0] + 'ma'
            s += 'a' * (i+1)
            res.append(s)
        return ' '.join(res)


if __name__ == "__main__":
    s = Solution()
    result = s.toGoatLatin("I speak Goat Latin")
    print(result)
