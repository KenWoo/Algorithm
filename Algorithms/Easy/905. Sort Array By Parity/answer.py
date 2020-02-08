from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_list = []
        odd_list = []
        for n in A:
            if n % 2 == 0:
                even_list.append(n)
            else:
                odd_list.append(n)
        l = []
        l.extend(even_list)
        l.extend(odd_list)
        return l


if __name__ == "__main__":
    s = Solution()
    result = s.sortArrayByParity([3, 1, 2, 4])
    print(result)
