from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=len)
        res = set()
        for f in folder:
            fs = f.split('/')
            ss = fs[0]
            if ss in res:
                continue
            flag = True
            for s in fs[1:]:
                ss += '/' + s
                if ss in res:
                    flag = False
                    continue
            if flag:
                res.add(f)
        return list(res)


if __name__ == "__main__":
    s = Solution()
    result = s.removeSubfolders(["/bf/bg/bh/bl", "/bf/bg/bh", "/aa/ab/aj/an", "/aa/ab/ac/ad", "/aa/aq/ar/as", "/bf/bv", "/bf/bv/cd/ce", "/aa/ab/aj/an/ao",
                                 "/bf/bg/bh/bl/bn", "/aa/ab/aj/ak", "/aa/aq/ay/bc/bd", "/bf/bg/bh/bl/bm", "/aa/aq/ay/bc", "/aa/ab/ac/ad/af", "/bf/bv/cd/ch/ci"])
    print(result)
