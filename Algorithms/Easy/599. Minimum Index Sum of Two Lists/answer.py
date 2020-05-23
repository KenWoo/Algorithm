from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        for i in range(len(list1)):
            dict1[list1[i]] = i
        dict2 = {}
        for i in range(len(list2)):
            dict2[list2[i]] = i
        c = []
        for k, v in dict1.items():
            if k in dict2:
                c.append((k, v + dict2[k]))
        c.sort(key=lambda x: x[1])
        res = [c[0][0]]
        for i in c:
            if i[1] == c[0][1]:
                res.append(i[0])
            else:
                break
        return res[1:]


if __name__ == "__main__":
    s = Solution()
    result = s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], [
                              "KFC", "Shogun", "Burger King"])
    print(result)
