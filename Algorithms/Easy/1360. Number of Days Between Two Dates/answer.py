from typing import List


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def span(d):
            l = d.split('-')
            days = 0
            year, month, day = int(l[0]), int(l[1]), int(l[2])
            for y in range(1970, year):
                days += 366 if (y % 4 == 0 and y %
                                100 != 0) or y % 400 == 0 else 365
            isleap = (year % 4 == 0 and year %
                      100 != 0) or year % 400 == 0
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            sum_months = [0] * 13
            for i in range(len(months)):
                item = months[i]
                if i == 1 and isleap:
                    item += 1
                sum_months[i+1] = sum_months[i] + item
            days += sum_months[month-1] + day - 1
            return days
        return abs(span(date1)-span(date2))


if __name__ == "__main__":
    s = Solution()
    result = s.daysBetweenDates("2060-08-18", "2001-08-25")
    print(result)
