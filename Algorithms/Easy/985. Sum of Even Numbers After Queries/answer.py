from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sum_val = sum([n for n in A if n % 2 == 0])
        for val, index in queries:
            if A[index] % 2 == 0:
                sum_val -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                sum_val += A[index]
            res.append(sum_val)
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.sumEvenAfterQueries(
        [1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]])
    print(result)
