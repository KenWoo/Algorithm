from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        for x, y in prerequisites:
            graph[x].append(y)
            indegrees[y] += 1
        for i in range(numCourses):
            zerodegree = False
            for j in range(numCourses):
                if indegrees[j] == 0:
                    zerodegree = True
                    break
            if not zerodegree:
                return False
            indegrees[j] = -1
            for n in graph[j]:
                indegrees[n] -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    result = s.canFinish(2, [[1, 0]])
    print(result)
