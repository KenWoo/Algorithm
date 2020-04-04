from typing import List


class Solution:
    def freqAlphabets(self, s: str) -> str:
        dict = {}
        for i in range(1, 10):
            dict[str(i)] = chr(97+i-1)
        for i in range(10, 27):
            dict[str(i)+'#'] = chr(97+i-1)
        N = len(s)
        i = 0
        res = []
        while i < N:
            if s[i] != '#':
                if i == N - 1:
                    prev = i
                    while s[prev] != '#' and prev > -1:
                        prev -= 1
                    for j in range(prev+1, N):
                        res.append(dict[s[j]])
            else:
                prev = i-1
                while s[prev] != '#' and prev > -1:
                    prev -= 1
                for j in range(prev+1, i-2):
                    res.append(dict[s[j]])
                res.append(dict[s[i-2: i+1]])
            i += 1
        return ''.join(res)


if __name__ == "__main__":
    s = Solution()
    result = s.freqAlphabets(
        "10#11#12")
    print(result)
