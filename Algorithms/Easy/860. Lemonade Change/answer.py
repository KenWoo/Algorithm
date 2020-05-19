from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f = t = 0
        for b in bills:
            if b == 5:
                f += 1
            elif b == 10:
                if not f:
                    return False
                f -= 1
                t += 1
            else:
                if f and t:
                    f -= 1
                    t -= 1
                elif f > 2:
                    f -= 3
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20])
    print(result)
