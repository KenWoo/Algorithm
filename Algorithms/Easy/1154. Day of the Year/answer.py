from typing import List


class Solution:
    def dayOfYear(self, date: str) -> int:
        d = date.split('-')
        year, month, day = int(d[0]), int(d[1]), int(d[2])
        isLeap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        mon = [0] * 13
        for i in range(12):
            item = months[i]
            if i == 1 and isLeap:
                item += 1
            mon[i+1] = mon[i] + item
        return mon[month-1] + day


if __name__ == "__main__":
    s = Solution()
    result = s.dayOfYear("2004-03-01")
    print(result)
