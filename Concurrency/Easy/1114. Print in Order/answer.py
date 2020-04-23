from typing import List
import threading


class Foo:
    def __init__(self):
        self.t2 = threading.Lock()
        self.t2.acquire()
        self.t3 = threading.Lock()
        self.t3.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.t2.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.t2.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.t3.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.t3.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


if __name__ == "__main__":
    pass
