from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            arr = email.split('@')
            prefix = arr[0].split('+')[0]
            prefix = prefix.replace('.', '')
            s.add(prefix + '@' + arr[1])
        return len(s)


if __name__ == "__main__":
    s = Solution()
    result = s.numUniqueEmails(
        ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"])
    print(result)
