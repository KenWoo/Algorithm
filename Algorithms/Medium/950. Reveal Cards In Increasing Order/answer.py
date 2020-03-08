from typing import List
import collections


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        N = len(deck)
        res = collections.deque()
        for i in range(N):
            if res:
                item = res.pop()
                res.appendleft(item)
            res.appendleft(deck[i])
        return list(res)


if __name__ == "__main__":
    s = Solution()
    result = s.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])
    print(result)
