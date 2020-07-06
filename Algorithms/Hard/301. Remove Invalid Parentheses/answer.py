from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return ['']

        def isValid(str):
            count = 0
            for i in range(len(str)):
                if str[i] == '(':
                    count += 1
                elif str[i] == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        visit = set()
        visit.add(s)
        q = [s]
        res = []
        N = len(s)
        while q:
            ss = q[0]
            q.pop(0)
            if isValid(ss):
                res.append((N-len(ss), ss))
            else:
                for i in range(len(ss)):
                    if ss[i] not in ['(', ')']:
                        continue
                    temp = ss[0:i] + ss[i+1:]
                    if temp not in visit:
                        q.append(temp)
                        visit.add(temp)
        if not res:
            return ['']
        mi = min([x[0] for x in res])
        res = [x[1] for x in res if x[0] == mi]
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.removeInvalidParentheses("x(")
    print(result)
