from typing import List


class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.cal:
            if s < end and start < e:
                return False
        self.cal.append((start, end))
        return True


if __name__ == "__main__":
    cal = MyCalendar()
    print(cal.book(10, 20))
    print(cal.book(15, 25))
    print(cal.book(20, 30))
