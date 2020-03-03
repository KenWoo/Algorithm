from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = [0 for x in range(26)]
        for t in tasks:
            l[ord(t)-ord('A')] += 1
        l.sort()
        i = 25
        while i >= 0 and l[i] == l[25]:
            i -= 1
        return max(len(tasks), (l[25]-1)*(n+1)+25-i)


if __name__ == "__main__":
    s = Solution()
    result = s.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
    print(result)
