from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        max_length = 0
        odd_list = []
        sub_odd_list = []
        for i in range(N):
            sub_odd_list.append(i)
        if sub_odd_list:
            odd_list.append(sub_odd_list)

        if odd_list:
            for n in range(1, N // 2 + 1):
                sub_odd_list = []
                for item in odd_list[n-1]:
                    if item-n >= 0 and item+n < N and s[item-n] == s[item+n]:
                        sub_odd_list.append(item)
                if sub_odd_list:
                    odd_list.append(sub_odd_list)
                else:
                    break

        even_list = []
        sub_even_list = []
        for i in range(N-1):
            if s[i] == s[i+1]:
                sub_even_list.append(i)
        if sub_even_list:
            even_list.append(sub_even_list)

        if even_list:
            for n in range(1, N // 2 + 1):
                sub_even_list = []
                for item in even_list[n-1]:
                    if item-n >= 0 and item+n+1 < N and s[item-n] == s[item+n+1]:
                        sub_even_list.append(item)
                if sub_even_list:
                    even_list.append(sub_even_list)
                else:
                    break

        if len(odd_list) == 0 and len(even_list) == 0:
            return ""
        if 2*len(odd_list)-1 > 2*len(even_list):
            n = len(odd_list) - 1
            i = odd_list[n][0]
            return s[i-n:i+n+1]
        else:
            n = len(even_list) - 1
            i = even_list[n][0]
            return s[i-n:i+n+2]


if __name__ == "__main__":
    s = Solution()
    result = s.longestPalindrome("abba")
    print(result)
