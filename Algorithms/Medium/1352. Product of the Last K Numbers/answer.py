from typing import List


class ProductOfNumbers:

    def __init__(self):
        self.list = [1]

    def add(self, num: int) -> None:
        if num != 0:
            self.list.append(self.list[-1] * num)
        else:
            self.list = [1]

    def getProduct(self, k: int) -> int:
        N = len(self.list)
        return self.list[N-1] // self.list[N-k-1] if k < N else 0


if __name__ == "__main__":
    productOfNumbers = ProductOfNumbers()
    productOfNumbers.add(3)
    productOfNumbers.add(0)
    productOfNumbers.add(2)
    productOfNumbers.add(5)
    productOfNumbers.add(4)
    print(productOfNumbers.getProduct(2))
    print(productOfNumbers.getProduct(3))
    print(productOfNumbers.getProduct(4))
    productOfNumbers.add(8)
    print(productOfNumbers.getProduct(2))
