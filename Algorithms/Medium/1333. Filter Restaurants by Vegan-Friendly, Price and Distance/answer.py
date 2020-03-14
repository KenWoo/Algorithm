from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filtered = []
        for id, rating, v, price, distance in restaurants:
            if price > maxPrice or distance > maxDistance:
                continue
            if veganFriendly == 1:
                if v == 1:
                    filtered.append((id, rating))
            else:
                filtered.append((id, rating))
        filtered.sort(key=lambda f: (-f[1], -f[0]))
        return [f[0] for f in filtered]


if __name__ == "__main__":
    s = Solution()
    restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [
        3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
    veganFriendly = 0
    maxPrice = 30
    maxDistance = 3
    result = s.filterRestaurants(
        restaurants, veganFriendly, maxPrice, maxDistance)
    print(result)
