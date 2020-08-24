from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        N = len(position)
        l, r = 1, position[N-1] - position[0]

        def check(n, threshold):
            last = position[0]
            count = 1
            for i in range(1, n):
                if position[i] - last < threshold:
                    continue
                count += 1
                if count == m:
                    return True
                last = position[i]
            return False

        while l < r:
            mid = (l + r) // 2
            if check(N, mid+1):
                l = mid + 1
            else:
                r = mid
        return l


if __name__ == "__main__":
    s = Solution()
    result = s.maxDistance([1, 2, 3, 4, 7], 3)
    print(result)
