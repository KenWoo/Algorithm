from typing import List
import queue


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        N = len(beginWord)

        def buildIndex():
            indexes = []
            for i in range(N):
                index = {}
                for word in wordList:
                    entry = word[:i] + word[i + 1:]
                    words = index.get(entry, [])
                    words.append(word)
                    index[entry] = words
                indexes.append(index)
            return indexes
        indexes = buildIndex()

        def getNextWord(word):
            res = []
            for i in range(len(word)):
                entry = word[:i] + word[i + 1:]
                if entry in indexes[i]:
                    for nextWord in indexes[i][entry]:
                        if nextWord != word:
                            res.append(nextWord)
            return res
        distance = {}

        def BFS():
            distance[beginWord] = 0
            q = queue.Queue()
            q.put(beginWord)
            while not q.empty():
                head = q.get()
                for nextWord in getNextWord(head):
                    if nextWord not in distance:
                        distance[nextWord] = distance[head] + 1
                        q.put(nextWord)
        res = []

        def DFS(current, target, path):
            if current == target:
                res.append(path[:])
                return
            for word in getNextWord(current):
                if distance[word] - 1 == distance[current]:
                    DFS(word, target, path + [word])
        BFS()
        DFS(beginWord, endWord, [beginWord])
        return res


if __name__ == "__main__":
    s = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = s.findLadders(beginWord, endWord, wordList)
    print(result)
