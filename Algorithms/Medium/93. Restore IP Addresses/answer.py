from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
       def dfs(s, segment, res, ip):
           if segment == 4:
                if s == '':
                    res.append(ip[1:])
                return
           for i in range(1,4):               
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:],segment+1,res,ip+'.'+s[:i])
                        if s[0] == '0':
                            break                                               
       res = []
       dfs(s, 0, res, '')
       return res


if __name__ == "__main__":
    s = Solution()
    result = s.restoreIpAddresses("25525511135")
    print(result)