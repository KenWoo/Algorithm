from typing import List
import random


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        while True:
            x = self.x_center - self.radius + random.random() * self.radius * 2
            y = self.y_center - self.radius + random.random() * self.radius * 2
            if (x - self.x_center) ** 2 + (y - self.y_center) ** 2 <= self.radius ** 2:
                return [x, y]


if __name__ == "__main__":
    pass
