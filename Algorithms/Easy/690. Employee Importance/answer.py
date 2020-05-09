from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee = None
        for e in employees:
            if e.id == id:
                employee = e
                break
        stack = employee.subordinates
        res = employee.importance
        while stack:
            s = stack.pop()
            for e in employees:
                if e.id == s:
                    stack.extend(e.subordinates)
                    res += e.importance
                    break
        return res


if __name__ == "__main__":
    s = Solution()
    employees = [Employee(1, 5, [2, 3]), Employee(2, 3, [])]
    result = s.getImportance(employees, 1)
    print(result)
