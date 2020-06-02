from typing import List


class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        vowels = []
        for i in range(len(arr)):
            if arr[i].lower() in ['a', 'e', 'o', 'i', 'u']:
                vowels.append(i)
        N = len(vowels)
        for i in range(N // 2):
            arr[vowels[i]], arr[vowels[N-i-1]
                                ] = arr[vowels[N-i-1]], arr[vowels[i]]
        return ''.join(arr)


if __name__ == "__main__":
    s = Solution()
    result = s.reverseVowels("aA")
    print(result)
