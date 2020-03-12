from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tt = []
        for t in transactions:
            name, time, amout, city = t.split(",")
            tt.append([name, time, amout, city, True])
        N = len(tt)
        for i in range(N):
            if int(tt[i][2]) > 1000:
                tt[i][4] = False
            else:
                for j in range(N):
                    if i == j:
                        continue
                    if tt[i][0] == tt[j][0] and tt[i][3] != tt[j][3] and abs(int(tt[i][1]) - int(tt[j][1])) <= 60:
                        tt[i][4] = False
                        break
        res = []
        for t in tt:
            if not t[-1]:
                res.append(",".join(t[:-1]))
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.invalidTransactions(
        ["alice,20,800,mtv", "alice,50,1200,mtv"])
    print(result)
