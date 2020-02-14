from typing import List


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = 0
        for y in range(1971, year):
            isLeap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
            days += 366 if isLeap else 365
        isLeap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] if isLeap else [
            31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days += sum(months[0: month-1])
        days += day-1
        rem = days % 7
        weekday = ["Sunday", "Monday", "Tuesday",
                   "Wednesday", "Thursday", "Friday", "Saturday"]
        return weekday[(rem + 5) % 7]


if __name__ == "__main__":
    s = Solution()
    result = s.dayOfTheWeek(15, 8, 1993)
    print(result)
