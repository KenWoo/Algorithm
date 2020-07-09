from typing import List

class TrieNode:
    def __init__(self):
        self.next = [None for i in range(26)]
        self.word = None

class Solution:
    def __init__(self):
        self.result = None 
        self.m = None
        self.n = None    

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(board) == 0 or len(board[0])==0:
            return []
        root = TrieNode()
        self.result = []
        
        for word in words:
            curr = root
            for char in word:
                idx = ord(char)-97
                if curr.next[idx] == None:
                    curr.next[idx] = TrieNode()
                curr = curr.next[idx]
            curr.word = word
        
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(board, i, j, root)
        return self.result

    def dfs(self, board, i, j, curr_node):
        tmp =  board[i][j]
        if tmp == '#' or curr_node.next[ord(tmp) - 97] == None:
            return
        board[i][j] = '#'
        curr_node = curr_node.next[ord(tmp) - 97]
        if curr_node.word != None:
            self.result.append(curr_node.word)
            curr_node.word = None  
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for move in moves:
            if 0 <= i+move[0] < self.m and 0 <= j+move[1] < self.n:
                self.dfs(board, i+move[0], j+ move[1], curr_node)
        board[i][j] = tmp         

if __name__ == "__main__":
    s = Solution()
    board = [
        ['a', 'a']
    ]
    words = ['aaa']    
    result = s.findWords(board, words)
    print(result)