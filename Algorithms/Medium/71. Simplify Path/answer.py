from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace('//', '/')
        arr = path.split('/')
        res = []
        for item in arr:
            if item in ['', '.']:
                continue
            elif res and item == '..':
                res.pop()
            elif item != '..':
                res.append(item)
        return '/' + '/'.join(res)

if __name__ == "__main__":
    s = Solution()
    result = s.simplifyPath('/../')
    print(result)