from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict = {}
        for c in cpdomains:
            arr = c.split()
            count = int(arr[0])
            s = arr[1]
            dict.setdefault(s, 0)
            dict[s] += count
            p = s.find('.')
            while p != -1:
                s = s[p+1:]
                dict.setdefault(s, 0)
                dict[s] += count
                p = s.find('.')
        res = []
        for k, v in dict.items():
            res.append(f'{v} {k}')
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.subdomainVisits(
        ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
    print(result)
