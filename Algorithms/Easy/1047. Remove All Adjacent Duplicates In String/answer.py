from typing import List


class Solution:
    def removeDuplicates(self, S: str) -> str:
        l = list(S)
        N = len(l)
        f, s = 0, 1
        while s < N:
            while f >= 0 and s < N and l[f] == l[s]:
                l[f] = l[s] = None
                while f >= 0 and l[f] is None:
                    f -= 1
                while s < N and l[s] is None:
                    s += 1
            f, s = s, s+1
        return ''.join([x for x in l if x is not None])


if __name__ == "__main__":
    s = Solution()
    result = s.removeDuplicates(
        "ibfjcaffccadidiaidchakchchcahabhibdcejkdkfbaeeaecdjhajbkfebebfea")
    print(result)
